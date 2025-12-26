import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\n📭 Tidak ada tugas.")
        return

    print("\n📋 Daftar Tugas:")
    for i, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {task['title']} [{status}]")

def add_task(tasks):
    title = input("Masukkan nama tugas: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("✅ Tugas berhasil ditambahkan!")

def complete_task(tasks):
    show_tasks(tasks)
    index = int(input("Pilih nomor tugas yang selesai: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("🎉 Tugas ditandai selesai!")
    else:
        print("❌ Nomor tidak valid.")

def delete_task(tasks):
    show_tasks(tasks)
    index = int(input("Pilih nomor tugas yang dihapus: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
        print("🗑️ Tugas dihapus.")
    else:
        print("❌ Nomor tidak valid.")

def main():
    while True:
        print("\n=== TO DO LIST APP ===")
        print("1. Lihat tugas")
        print("2. Tambah tugas")
        print("3. Tandai selesai")
        print("4. Hapus tugas")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        tasks = load_tasks()

        if pilihan == "1":
            show_tasks(tasks)
        elif pilihan == "2":
            add_task(tasks)
        elif pilihan == "3":
            complete_task(tasks)
        elif pilihan == "4":
            delete_task(tasks)
        elif pilihan == "5":
            print("👋 Terima kasih!")
            break
        else:
            print("❌ Pilihan tidak valid!")

if __name__ == "__main__":
    main()