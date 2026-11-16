dic = {
    "applicationIdSuffix": ".daily",
    "applicationLabel": "Heroes 3",
    "applicationVariant": "daily",
    "signingConfig": "dailySigning",
}
print(";".join([f"{key}={value}" for key, value in dic.items()]))
