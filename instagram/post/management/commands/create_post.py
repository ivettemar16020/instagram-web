from django.core.management.base import BaseCommand

from post.models import Post
from post.models import PostUserLike
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
                nombre = raw_input("Ingrese el primer nombre del usuario: ")
                apellido = raw_input("Ingrese el apellido del usuario: ")
                username = raw_input("Ingrese el nombre de usuario: ")
                email = raw_input("Ingrese un email valido: ")
                mi_user = User(first_name=nombre, last_name=apellido, username=username, email=email)
                mi_user.save()
                print("\n")
                
            elif ans=="2":
                print("""
                \n 
                Listar usuarios
                -----------------
                """) 
                print("Cantidad de usuarios creados:", User.objects.all().count())
                for user in User.objects.all():
                    print("******************************")
                    print("pk={}: {}, {} / {} - {} \n".format(user.pk, user.last_name, user.first_name, user.username, user.email))

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
                        print("Cantidad de post creados:", Post.objects.filter(created_by= User.objects.get(username=username)).count())
                        title = raw_input("Ingrese el titulo del post: ")
                        description = raw_input("Ingrese el contenido: ")
                        mi_post = Post(title=title, description=description, created_by= User.objects.get(username=username))
                        mi_post.save()
                        print("Ahora existen ", Post.objects.filter(created_by = User.objects.get(username=username)).count(), "post creados")

                    elif answ2=="2":
                        print("""
                        \n 
                        Like de post
                        ----------
                        """)
                        all_posts = Post.objects.all() 
                        for each_post in all_posts:
                            likes = PostUserLike.objects.filter(post_id= each_post.pk).count()
                            print("******************************")
                            print("pk={}: {} ({}) \n {} \n".format(each_post.pk, each_post.title, likes, each_post.description))
                
                        post_pk = raw_input("\n Por favor ingrese el pk del post al que desea dar 'me gusta':  ")
                        chosen_post = Post.objects.get(pk= post_pk)
                        like = PostUserLike(user= User.objects.get(username=username), post= chosen_post)
                        like.save()
                        print("\n")


                    elif answ2=="3":
                        print("""
                        \n 
                        Deletes post
                        ----------
                        """)
                        mis_posts = Post.objects.filter(created_by= User.objects.get(username=username))
                        for each_post in mis_posts:
                            likes = PostUserLike.objects.filter(post_id= each_post.pk).count()
                            print("******************************")
                            print("pk={}: {} ({}) \n {} \n".format(each_post.pk, each_post.title, likes, each_post.description))
                
                        post_pk = raw_input("\n Por favor ingrese el pk del post que desea 'eliminar':  ")
                        chosen_post = Post.objects.get(pk= post_pk)
                        chosen_post.delete()
                        print("\n El post ha sido eliminado \n")

                    elif answ2=="4":
                        print("Adios ", username)
                        loop2 = False    
                        loop3 = False
                    
                    elif ans !="":
                        print("\n Opcion invalida")

            elif ans=="4":
                print("\n Adios!") 
                break
            elif ans !="":
                print("\n Opcion invalida") 
