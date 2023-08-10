import rsa
HELLO_STIC = ['CAACAgIAAxkBAAIMp2NzShC-xoN8tIdKGh2rplJeYjcDAAJnBAACnNbnCltK7aMvqs22KwQ',
              'CAACAgIAAxkBAAIMqmNzSiMIudMsOERn4RCBO4emegdwAAKkAAOvxlEaBO5i_vR9pdsrBA',
              'CAACAgIAAxkBAAIMrWNzSkqchFPEKtwslZ-fKI61Q0qeAALgCAACLw_wBgABdoS5BOuogCsE']

END_STIC = ['CAACAgIAAxkBAAIMsGNzSz-HEDLlNlAQloKGurp3oixiAAKwAAMvD_AGjAfp6TK3ePcrBA',
            'CAACAgIAAxkBAAIMs2NzS0KWk4mZFRh0FYk6bU0mHSEqAAKzAAOvxlEaJaXttrUY8porBA',
            'CAACAgIAAxkBAAIMtmNzS0jRtFB1p9KopPwQm22RBDHmAAJ0BAACnNbnCs8fpxHxBKbxKwQ']

NAME_STIC = ['CAACAgIAAxkBAAIMuWNzS8GHFybJRmMs0SI6GGrCyi0bAAJSBAACnNbnCj7kddfodFK2KwQ',
             'CAACAgIAAxkBAAIMv2NzS9xhugkmdrKmFsQYjAKusFcmAAKuAAOvxlEarAJXzOg7SSsrBA',
             'CAACAgIAAxkBAAIMwmNzS_AHnPVpGv0mzBbsD7pIrTEaAALCAAMvD_AG4BAq6cUvCLQrBA']

LEVEL_STIC = ['CAACAgIAAxkBAAIMxWNzTGVH8M7DTUlg8HvZvGsUNjB7AAK1AAOvxlEaVaf_cU0_9qIrBA',
              'CAACAgIAAxkBAAIMyGNzTGtxrIq3F1-WhQE_pQEQ7vmTAAJ3BAACnNbnCuovPWYwd5oXKwQ']

LUCK_STIC = ['CAACAgIAAxkBAAIMy2NzTTZpQYLNp8hhshQaEsQVHaqsAAJzBAACnNbnCqiPcGJysBCHKwQ',
             'CAACAgIAAxkBAAIMzmNzTTniDLBpmS5CMJvIAZOgtStKAAJbBAACnNbnCuSalzLZMh0sKwQ',
             'CAACAgIAAxkBAAIM0WNzTUOSWraMkVu2gv1wyfC5PynaAAJdBAACnNbnCnveER58wEZDKwQ',
             'CAACAgIAAxkBAAIM1GNzTVCADhxlNdEid_aDwTqyxTyWAAJgBAACnNbnCgFiTjfmDrEiKwQ',
             'CAACAgIAAxkBAAIM12NzTVqVj09Q97brsMKzfZgf5OKcAAJ2BAACnNbnClFiwAJxzW2QKwQ',
             'CAACAgIAAxkBAAIM2mNzTYPkI0DjRV7zv1uXHTwG3zZ1AAK8AAMvD_AG--2NFORc8NcrBA',
             'CAACAgIAAxkBAAIM3WNzTZYmvGMad46K6MVx_uS-7hE-AAK2AAMvD_AGyXatf6A7QuIrBA',
             'CAACAgIAAxkBAAIM42NzTaI3_bDJB6L18gXUsodK_xEkAALgAAMvD_AGmID4nSqJ2XMrBA']
UNLUCK_STIC = ['CAACAgIAAxkBAAIM5mNzTjLCnGjobJ__m7K8nyeJ7VQiAAJRBAACnNbnClUXds6PYOU2KwQ',
               'CAACAgIAAxkBAAIM6WNzTjkzz-SyrJVfrOFnJRR2OVgvAAJcBAACnNbnClokfVuRQO25KwQ',
               'CAACAgIAAxkBAAIM7GNzTj1SQTAOnhYIpwfGfdCXAAELNwACcAQAApzW5wp76bvlRrFvNSsE',
               'CAACAgIAAxkBAAIM72NzTk0HkY-_QusXbDgvqomRJjVjAAKmAAOvxlEaQy1kokk9sJkrBA',
               'CAACAgIAAxkBAAIM8mNzTlSnJF5fBHo8PvTRgHOAejaYAALMAAMvD_AGIlTPs_iFazIrBA']

WIN_STIC = ['CAACAgIAAxkBAAIM-GNzTz10nDKcK94WJxILR9W97ALVAAJUBAACnNbnCsdTQ7uDhWuuKwQ',
            'CAACAgIAAxkBAAIM-2NzT0S0nbuyoGBwggX2wg2T7_UpAAJlBAACnNbnCrpf9lvSZKOIKwQ',
            'CAACAgIAAxkBAAIM_mNzT1HiekKilSQHHWIIptGgmYO0AAKsAAMvD_AGXcJ3K3Nof9ArBA',
            'CAACAgIAAxkBAAINAWNzT1Vtmgkb39g8GgABDZUq9yzSnQAC2gADLw_wBrIOXCk8aWm2KwQ']

NON_WORD_STIC = ['CAACAgQAAxkBAAINBGNzZSs09r_yjf7bs5pgG_0T2zbvAAKmCAACO0spUabE6ykjzCRSKwQ',
                 'CAACAgQAAxkBAAINB2NzZbUuTs8hD61VyDwPQAKhWtwEAAJsDQACLy8gUb3QsFCxVV_cKwQ',
                 'CAACAgUAAxkBAAINCmNzZcEv_C5_qO6Wldwjvn0UY2hNAAKBCAACxlHGFZXfauYX-8AwKwQ',
                 'CAACAgQAAxkBAAINDWNzZc1pyU4DBl8uYbRMIlEHD-qLAALfCQACnaMhUbXyQRD8bkqKKwQ',
                 'CAACAgQAAxkBAAINEGNzZdtJdgSGH-lCVmRHwCl3KpGEAAKlAwACghXBHV_t6xcVOdAaKwQ',
                 'CAACAgQAAxkBAAINFmNzZfOhQd9KpJNuNvBetcz-XtO4AAICAQACghXBHd0jCT8PQ5TsKwQ',
                 'CAACAgQAAxkBAAINGWNzZfut1cmTOc6cb9m7jEPVr9j9AAJwFQACcwdRUZ7ug-LqwECoKwQ']


# # Боб формирует публичный и секретный ключ
# (bob_pub, bob_priv) = rsa.newkeys(512)

# with open("cows_and_bulls_update/ssh/key", "w", encoding="utf-8") as file:
#     file.write(str(bob_priv))

# with open("cows_and_bulls_update/ssh/key.pub", "w", encoding="utf-8") as file:
#     file.write(str(bob_pub))
# exit()
# with open("cows_and_bulls_update/ssh/key", encoding="utf-8") as file:
#     private_key = file.read().split(', ')
#     private_key = [int(number) for number in private_key]
#     private_key = rsa.PrivateKey(*private_key)
# with open(f"cows_and_bulls_update/coins.txt", "rb") as file:
#     money = file.read()
#     message = rsa.decrypt(money, private_key)
#     money = message.decode('utf8')
#     print(money)
# exit()
# with open("cows_and_bulls_update/ssh/key.pub", encoding="utf-8") as file:
#     public_key = file.read().split(', ')
#     public_key = [int(number) for number in public_key]
#     public_key = rsa.PublicKey(*public_key)
# with open(f"cows_and_bulls_update/coins.txt", mode="wb") as file:
#     message = f"{0}".encode('utf8')
#     crypto = rsa.encrypt(message, public_key)
#     file.write(crypto)


# # -*- coding: utf-8 -*-
# exit()


# # Боб формирует публичный и секретный ключ

# (bob_pub, bob_priv) = rsa.newkeys(512)

# # Алиса формирует сообщение Бобу и кодирует его в UTF8,
# # поскольку RSA работает только с байтами
# message = 'hello Bob!'.encode('utf8')

# # Алиса шифрует сообщение публичным ключом Боба
# crypto = rsa.encrypt(message, bob_pub)
# print(crypto)
# print(type(crypto))

# # Боб расшифровывает сообщение своим секретным ключом
# message = rsa.decrypt(crypto, bob_priv)
# print(message.decode('utf8'))
