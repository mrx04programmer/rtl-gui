# RTL GUI Online
Herramienta especializada en escaneos de vulnerabilidades no comunes y explotador de las mismas.

<hr style="background-color: lightblue">

### Pre-requisitos

|Nombre del requisito | Versión minima|
|---------------------|---------------|
| Python | 3.7 o superior|
| Git | Cualquiera|
| PHP | 7.4.3 |

<hr style="background-color: lightblue">

Si deseas probar RTL , sigue los siguientes pasos:

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ffindicons.com%2Ffiles%2Ficons%2F725%2Fcolobrush%2F256%2Ficone_windows.png&f=1&nofb=1&ipt=89b53afecb4292de2f5c44fcdc9ebce9ed646f0fbc351d9d2901a845c049e3be&ipo=images" width="20"><span> En Windows 7.1/8.0/10/11 </span>

1. Debes configurar la variable de entorno para PHP, para ello :
    * Abre la aplicación `Variables de entorno` o similar.
    * Seleccionas el texto `Path` de arriba si deseas que solo sea para un usuario en especifico o el de abajo para todos y le das `Editar`:

    ![img](https://www.netveloper.com/cw/jiujj0avruoabovhsssn5218/variables-de-entorno.jpg)
    
    * Una vez que seleccionaste el boton `Editar` aparecera un menú como el siguiente
    ![img2](https://www.netveloper.com/cw/jiujj0avruoabovhsssn5218/editar-variables-de-entorno.jpg)
    
    * Seleccionas en `Nuevo` y colocas la ruta del ejecutable de php, en este caso se encuentra en mi servidor de `XAMPP`
2. Clona el repositorio de Github, para esto ve a la consola de tu preferencia y ejecuta `git clone https://github.com/mrx04programmer/rtl-gui`
3. Una vez descargado, entras a el con el comando `cd rtl-gui`
4. Por ultimo crea el servidor local con `php -S localhost:8080`

<hr style="background-color: lightblue">

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.brosix.com%2Fwp-content%2Fuploads%2FLinux_Logo_07.png&f=1&nofb=1&ipt=bea151f702473a413a4f5c8cf47c48a72f86900c52d3c7c8ad1664aa4fa876d1&ipo=images" width="20"><span> En Linux</span>

1. Clona el repositorio de Github, para esto ve a la consola de tu preferencia y ejecuta `git clone https://github.com/mrx04programmer/rtl-gui`
2. Una vez descargado, entras a el con el comando `cd rtl-gui`
3. Por ultimo crea el servidor local con `php -S localhost:8080`

<hr style="background-color: lightblue">

<h6>Demo</h6>
* Interfaz principal
![image](https://user-images.githubusercontent.com/46001898/211378982-e6aa6f34-cafc-4c14-ac35-98b25d09c879.png)

* Interfaz del Scanner
![image](https://user-images.githubusercontent.com/46001898/211379188-31cf8ad3-b726-40c9-b35c-f870d70ccf19.png)

* Interfaz del Explotador
![image](https://user-images.githubusercontent.com/46001898/211379314-6ad56af0-b6e9-422a-924f-bd286bfd322f.png)

<h6>Nota: El modulo de Obtener credenciales al conectarse esta en beta y el proxy solo funciona si la ip es externa a tu network local.</h6>
