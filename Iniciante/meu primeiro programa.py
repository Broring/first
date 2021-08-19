curl -T sample.provisionprofile 'https://concrete-userfiles-production.s3-us-west-2.amazonaws.com/build_certificates/uploads/30067/original/certs.p12?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAIOC7N256G7J2W2TQ%2F20180216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20180216T124240Z&X-Amz-Expires=600&X-Amz-SignedHeaders=content-length%3Bhost&X-Amz-Signature=2bf42176650f00405abfd7b7757635c9be16b43e98013abb7f750d3c658be28e'

print('*****My first Program*****')

print('Bem vindo ao programa do Exercito!!')
idade = int(input('Digite sua idade: '))
peso = float(input('Digite seu Peso: '))
altura = float(input('Digite sua Altura: '))

if idade >= 18 and peso >= 60 and altura >= 1.70:
    print('Você está apto para entrar no exercito !!!')
else:
    print('Você não está apto para entrar no exercito :/')
