from __future__ import annotations

import json
from pathlib import Path
import tkinter as tk
from tkinter import ttk

from actions import (
    ensure_logger,
    get_git_version,
    handle_d_action,
    log_click,
    log_start,
)


REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = REPO_ROOT / "panel" / "app" / "config.json"
LOG_FILE = REPO_ROOT / "logs" / "panel.log"


def load_config() -> dict:
    with CONFIG_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def build_ui(root: tk.Tk, config: dict, logger) -> None:
    root.title(config.get("title", "GEOINWEST"))
    root.geometry(config.get("size", "320x220"))
    root.resizable(False, False)
    root.attributes("-topmost", True)

    outer_padding = 8
    button_pad = 4
    container = ttk.Frame(root, padding=outer_padding)
    container.pack(fill=tk.BOTH, expand=True)

    header_frame = ttk.Frame(container)
    header_frame.pack()

    header = ttk.Label(
        header_frame,
        text=config.get("header", "GEOINWEST"),
        font=("Segoe UI", 14, "bold"),
    )
    header.pack()

    subheader = ttk.Label(
        header_frame,
        text=config.get("subheader", "OPERAT_WORD_MAKRO"),
        font=("Segoe UI", 9),
    )
    subheader.pack(pady=(0, button_pad))

    buttons_frame = ttk.Frame(container)
    buttons_frame.pack()

    buttons = config.get("buttons", [])
    for index, label in enumerate(buttons):
        row = index // 5
        column = index % 5
        action = None
        if label == "D":
            action = lambda: handle_d_action(REPO_ROOT, logger)
        button = ttk.Button(
            buttons_frame,
            text=label,
            command=lambda value=label, handler=action: (
                log_click(logger, value),
                handler() if handler else None,
            ),
            width=4,
        )
        button.grid(row=row, column=column, padx=button_pad, pady=button_pad)

    root.update_idletasks()
    buttons_width = buttons_frame.winfo_reqwidth()
    header_frame.configure(width=buttons_width)
    header_frame.pack_propagate(False)
    root.update_idletasks()
    window_width = root.winfo_reqwidth()
    window_height = root.winfo_reqheight()
    root.minsize(window_width, window_height)
    root.geometry(f"{window_width}x{window_height}")


def main() -> None:
    config = load_config()
    logger = ensure_logger(LOG_FILE)
    version = get_git_version(REPO_ROOT)
    log_start(logger, version)

    root = tk.Tk()
    build_ui(root, config, logger)
    root.mainloop()


if __name__ == "__main__":
    main()

