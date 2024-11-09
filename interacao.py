mensagem_criptografada = "cole aqui sua mensagem criptografada"
private_key_string = (1441, 5141)

# Converter a mensagem criptografada para uma lista de inteiros
ciphertext_blocks = list ( map(int , mensagem_criptografada . split () )
)

# Descriptografar usando a chave privada
def decrypt ( private_key , ciphertext_blocks ) :
    d , n = private_key
    plaintext_bytes = b""
    for block in ciphertext_blocks :
        plaintext_int = pow( block , d , n ) # Descriptografa o bloco
        block_bytes = plaintext_int . to_bytes (( plaintext_int .
        bit_length () + 7) // 8 , byteorder ='big')
        plaintext_bytes += block_bytes
    return plaintext_bytes . decode ('utf -8')

# Executar a descriptografia
mensagem_original = decrypt ( private_key_string , ciphertext_blocks )
print (" Mensagem descriptografada :\n", mensagem_original )
