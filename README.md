# Reporte de Práctica: Backend REST Dockerizado y App Android con Sesiones Seguras

## Información Académica
* **Unidad Académica:** Escuela Superior de Cómputo (ESCOM) - IPN
* **Unidad de Aprendizaje:** Desarrollo de Aplicaciones Móviles Nativas
* **Grupo:** 7CV4
* **Profesor:** Gabriel Hurtado Avilés
* **Alumno:** Vázquez Hernández Michel
* **Boleta:** 2022630101
* **Fecha de Entrega:** Jueves 27 de marzo de 2026

---

## 1. Introducción
Esta práctica integra el desarrollo de una aplicación móvil nativa en **Android (Kotlin)** con un servidor **API REST** desplegado en contenedores **Docker**. El sistema permite la gestión de notas mediante operaciones CRUD (Create, Read, Update, Delete) y cuenta con una capa de seguridad avanzada que incluye encriptación de credenciales y manejo de sesiones mediante tokens únicos.

---

## 2. Arquitectura del Proyecto

### A. Backend (Servidor REST)
Desarrollado en **Python (Flask)**, el servidor se encarga de:
* Procesar las peticiones HTTP de la aplicación móvil.
* Gestionar el registro de usuarios con **hashing de contraseñas** (`scrypt`).
* Emitir **Tokens de Sesión (UUID)** para validar la identidad en cada petición.
* Correr en un entorno aislado gracias a **Docker y Docker Compose**.



### B. Frontend (App Móvil)
Desarrollada en **Kotlin (Android Studio)**, utiliza:
* **Retrofit 2** para la comunicación asíncrona con el backend.
* **Material Design** para una interfaz moderna y responsiva.
* **Headers de Autorización** para enviar el token de seguridad en cada operación CRUD.

---

## 3. Evidencias de Ejecución (QA)

### Registro y Autenticación Segura
Se verificó que el sistema encripta las contraseñas antes de almacenarlas.
<img width="1125" height="161" alt="image" src="https://github.com/user-attachments/assets/54a1d3b7-9a49-4d39-8dda-6e62119fdf6e" />
**

### Gestión de Sesiones (Punto Clave)
El sistema bloquea el acceso si no hay un token válido.
* **Acceso Denegado:** > **<img width="337" height="623" alt="image" src="https://github.com/user-attachments/assets/cf1c6d66-2019-43bf-99db-7dd0a720901c" />
**
* **Operación Exitosa:** > **<img width="339" height="642" alt="image" src="https://github.com/user-attachments/assets/dbdd175e-1990-423a-8ff4-55a034393c1f" />
**

## 4. Conclusiones
El principal reto fue establecer la comunicación entre el emulador y el contenedor Docker, resuelto mediante la dirección IP `10.0.2.2`. El logro más significativo fue la implementación del middleware de seguridad en Flask, que garantiza que solo usuarios autenticados puedan manipular la información, cumpliendo con los estándares de robustez solicitados en la asignatura.

---

## 5. Bibliografía (Formato APA)
* Android Developers. (2024). *Build a REST API with Retrofit*. Recuperado de https://developer.android.com/
* Docker Documentation. (2024). *Docker Compose overview*. Recuperado de https://docs.docker.com/
* Pallets Projects. (2024). *Flask: User Authentication and Security*. Recuperado de https://flask.palletsprojects.com/
* Square, Inc. (2024). *Retrofit: A type-safe HTTP client for Android*. Recuperado de https://square.github.io/retrofit/
