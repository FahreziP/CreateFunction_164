#1
def konversi_suhu(valve, suhu):
    if suhu == "C":
        # konversi celcius ke fahrenheit
        return (valve * 9/5) + 32
    elif suhu == "F":
        # konversi fahrenheit ke celcius
        return (valve - 32) * 5/9
    else:
        raise ValueError("Suhu tidak Valid."\
        "Suhu harus 'C' atau 'F'.")
print(konversi_suhu(200, "C"))
print(konversi_suhu(38, "F"))

#2
luas_lingkaran = lambda jari_jari: 3.14 * (jari_jari ** 2)

n = float(input("Masukkan jari-jari lingkaran: "))

print("Luas lingkaran dengan jari-jari" ,n, "adalah:", luas_lingkaran(n))
