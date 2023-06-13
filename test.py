from cryptography.fernet import Fernet

#대칭키
key = b'Igo-WFENumnM_XfjUwKJ64l0P_soy-mD6qE3rbraZpA='

encrypt_str = b'gAAAAABkiGdZhw4A6_u9GYm1OA6neLfdRDp8iVJElto5ccP332Qh160I0SqZKwdwCUjDE8ewJjNWSPPVziceYv3tPBlUXKSPJdJWP2Messzutx-bXG60e7S8M4ozrSscTQw2mb_aT35AH4kHAlScPnRzkZGIaBDe-g=='
fernet = Fernet(key)
decrypt_str = fernet.decrypt(encrypt_str)

print("복고화된 문자열 : ", decrypt_str)

