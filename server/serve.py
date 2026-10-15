"""Serve only /weather.png; default binding is loopback, no directory listing."""

import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit


def handler_for(image_path):
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_image()

        def do_HEAD(self):
            self.send_image(head=True)

        def send_image(self, head=False):
            if urlsplit(self.path).path != "/weather.png":
                self.send_error(404)
                return
            try:
                content = Path(image_path).read_bytes()
            except FileNotFoundError:
                self.send_error(503, "No successful weather image yet")
                return
            self.send_response(200)
            self.send_header("Content-Type", "image/png")
            self.send_header("Content-Length", str(len(content)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            if not head:
                self.wfile.write(content)

    return Handler


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", type=Path, default=Path("runtime/weather.png"))
    parser.add_argument("--bind", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    with ThreadingHTTPServer((args.bind, args.port), handler_for(args.image)) as server:
        print(f"Serving /weather.png on {args.bind}:{server.server_port}", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
