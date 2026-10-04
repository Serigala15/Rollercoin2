import json
import os

# Menentukan nama file config (ubah jika nama file Anda berbeda)
CONFIG_FILE = "config (2).json"

def load_config():
    if not os.path.exists(CONFIG_FILE):
        print(f"File {CONFIG_FILE} tidak ditemukan!")
        return None
    
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        try:
            config = json.load(f)
            return config
        except json.JSONDecodeError as e:
            print(f"Error membaca format JSON: {e}")
            return None

# Contoh penggunaan di dalam script:
config = load_config()

if config:
    # Mengambil nilai dari config
    access_token = config.get("access_token")
    is_game_enabled = config.get("game")
    max_level = config.get("max_level_game")
    
    print(f"Berhasil memuat konfigurasi. Mode Game: {config.get('mode_game')}")