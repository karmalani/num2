import numpy as np

#x_k_old = np.array([1, 1, 1])
x_k_old = np.array([0, 1, 1])
A = np.array([[10, 0, 0], [1, 5, 0], [-1, 0, 1]])
for komponente in range(3):
    print("Eintrag:",komponente+1)
    for i in range(3):
        print("Iteration:", i + 1)
        x_k_tilde = A.dot(x_k_old)
        x_k_new = x_k_tilde/np.linalg.norm(x_k_tilde)
        lambda_k = x_k_tilde[komponente]/x_k_old[komponente]
        x_k_old=x_k_new
        print(lambda_k)