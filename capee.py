import random

print("=" * 80)
print(r"""
███████╗██╗███╗   ██╗██████╗     ████████╗██╗  ██╗███████╗
██╔════╝██║████╗  ██║██╔══██╗    ╚══██╔══╝██║  ██║██╔════╝
█████╗  ██║██╔██╗ ██║██║  ██║       ██║   ███████║█████╗  
██╔══╝  ██║██║╚██╗██║██║  ██║       ██║   ██╔══██║██╔══╝  
██║     ██║██║ ╚████║██████╔╝       ██║   ██║  ██║███████╗
╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝        ╚═╝   ╚═╝  ╚═╝╚══════╝
    ███╗   ███╗ ██████╗ ██╗   ██╗███████╗███████╗
    ████╗ ████║██╔═══██╗██║   ██║██╔════╝██╔════╝
    ██╔████╔██║██║   ██║██║   ██║███████╗█████╗  
    ██║╚██╔╝██║██║   ██║██║   ██║╚════██║██╔══╝  
    ██║ ╚═╝ ██║╚██████╔╝╚██████╔╝███████║███████╗
    ╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
""")
print("=" * 80)

user = input("siapa nama lu: ")

def main_game():
    while True:
        posisi_tikus = random.randint(1, 100)
        riwayat_tebakan = []
        print("=" * 80)
        print(f'''
        Woii {user}! Selamat datang di game FIND THE MOUSE!
        Jadi di bawah tanah ada 100 goa tempat si tikus tinggal,
        Menurut lu si Tikus ada di goa ke berapa?''')

        while True:
            try:
                print("=" * 80)
                tebak = int(input("Masukin jawaban lu: "))
                if tebak < 1 or tebak > 100:
                    print("Masukin angka 1 sampai 100 jirr")
                    continue
                
                riwayat_tebakan.append(tebak)
                
                if tebak < posisi_tikus:
                    print(f"Yahh cupuu... tebakan lu terlalu kecil {user}!")
                elif tebak > posisi_tikus:
                    print(f"Yahh... tebakan lu terlalu besar {user}!")
                else:
                    print(f'''
                    Mantapp... selamat {user}! lu berhasil menebak si Tikus!!!
                    Si Tikus ada di goa ke {posisi_tikus} dan tebakan lu {tebak}.
                          ''')
                    print(f"semua tebakan lu: {riwayat_tebakan}")
                    
                    while True:
                        main_lagi = input("Mau maen lagi ngga (y/n): ").lower()
                        if main_lagi == 'y':
                            print("okeh kita main lagi!")
                            break
                        elif main_lagi == 'n':
                            print("makasih udah maen ya!")
                            return
                        else:
                            print("iya ato ngga (y/n)!")
                    break  
                
                print(f"Riwayat tebakan lu: {riwayat_tebakan}")
            
            except ValueError:
                print("masukin angka doang co!")

        if main_lagi == 'n':
            break  

main_game()