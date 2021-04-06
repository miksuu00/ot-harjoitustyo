
class Budget:
    user = ""
    psw = ""
    profiles = {"Username": user, "Password": psw}
    def __init__(self, user:str, psw: str):
        self.user = user
        self.psw = psw
        

    def new_user():

        while True:
            print("Syötä käyttäjänimi ja salasana, salasanan pituus tulee olla vähintään 8 merkkiä!")
            nimi = input("Käyttäjä:")
            sala = input("Salasana:")
            while len(sala)<8:
                print("Liian lyhyt salasana, yritä uudestaan")
                sala = input("Salasana:")

            profiles = {nimi : sala}
            print(profiles)
           # print(nimi, sala)
            break

    
userr = Budget.new_user()

#if __name__ == "__main__":

    #Budget.new_user()