usuarios=$(cat /etc/passwd | grep /bin/bash | cut -f 1 -d":")
echo $usuarios
read -p "con cual te quieres loguear" logarse
su $logarse
