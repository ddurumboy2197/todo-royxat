import string
import secrets

def parol_generator(uzunlik, max_belgi):
    if uzunlik < 8:
        raise ValueError("Parol uzunligi kamida 8 ta belgi bo'lishi kerak")
    if max_belgi < 3:
        raise ValueError("Maxsus belgilar soni kamida 3 ta bo'lishi kerak")

    belgilar = string.ascii_letters + string.digits + string.punctuation
    parol = ''.join(secrets.choice(belgilar) for _ in range(uzunlik))

    max_belgi_soni = 0
    for belgida in parol:
        if belgida in string.punctuation:
            max_belgi_soni += 1
        if max_belgi_soni >= max_belgi:
            break

    if max_belgi_soni < max_belgi:
        parol += ''.join(secrets.choice(string.punctuation) for _ in range(max_belgi - max_belgi_soni))

    return parol

print(parol_generator(12, 5))
```

```python
uzunlik = int(input("Parol uzunligini kiriting: "))
max_belgi = int(input("Maxsus belgilar sonini kiriting: "))

print(parol_generator(uzunlik, max_belgi))
