from django.core.management.base import BaseCommand

from post.models import Post
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print("Bienvenido")
        loop = True
        loop2 = False
        while loop:
            print("Menu principal")
            print("""
            1. Crear usuario
            2. Listar usuarios
            3. Acceder
            4. Salir
            """)
            ans=raw_input("Elija una opcion (1-4) ") 
            if ans=="1": 

                print("""
                \n 
                Crear usuario
                --------------
                """) 
                username = raw_input("Ingrese el nombre de usuario: ")
                email = raw_input("Ingrese un email valido: ")
                mi_user = User(username=username, email=email)
                mi_user.save()
                
            elif ans=="2":
                print("""
                \n 
                Listar usuarios
                -----------------
                """) 
                print("Cantidad de usuarios creados:", User.objects.all().count())
                for user in User.objects.all():
                    print("pk={}: {} - {} ".format(user.pk, user.username, user.email))

            elif ans=="3":
                print("""
                \n 
                Acceder
                ------
                """)
                loop2 = True
                while loop2: 
                    try:
                        username = raw_input("Ingrese su nombre de usuario: ")
                        email = raw_input("Ingrese email: ")
                        User.objects.get(username=username, email=email)
                        loop2 = False
                        loop3 = True
                    except: 
                        print("El usuario o el email son incorrectos")

                while loop3: 
                    print("Menu de ", username)
                    print("""
                    1. Crear Post
                    2. Like de Post
                    3. Delete Post
                    4. Menu principal
                    """)
                    answ2 = raw_input("Seleccione una opcion valida: ")
                    if answ2=="1":
                        print("""
                        \n 
                        Crear post
                        ----------
                        """)

                    elif answ2=="2":
                        print("""
                        \n 
                        Like de post
                        ----------
                        """)

                    elif answ2=="3":
                        print("""
                        \n 
                        Deletes post
                        ----------
                        """)

                    elif answ2=="4":
                        print("Adios ", username)
                        loop2 = False    
                        loop3 = False
                    
                    elif ans !="":
                        print("\n Opcion invalida")

                    """
                    print("Cantidad de post creados:", Post.objects.all().count())
                    title = raw_input("Ingrese el titulo del post: ")
                    description = raw_input("Ingrese el contenido: ")
                    mi_post = Post(title=title, description=description)
                    mi_post.save()
                    print("Ahora existen ", Post.objects.all().count(), "post creados")
                    """
            elif ans=="4":
                print("\n Adios!") 
                break
            elif ans !="":
                print("\n Opcion invalida") 
