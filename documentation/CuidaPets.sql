CREATE TABLE Disponibilidad
(
  id                 INT      NOT NULL,
  desde              DATETIME NOT NULL,
  hasta              DATETIME NOT NULL,
  idTipoMascota      INT      NOT NULL,
  idServicioOfrecido INT      NOT NULL,
  capacidad          INT      NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE Domicilio
(
  id        INT     NOT NULL,
  calle     VARCHAR NOT NULL,
  numero    INT     NOT NULL,
  piso      INT     NULL    ,
  dpto      VARCHAR NULL    ,
  barrio    VARCHAR NOT NULL,
  ciudadId  INT     NOT NULL,
  idUsuario INT     NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE Mascota
(
  id                   INT     NOT NULL,
  nombre               VARCHAR NOT NULL,
  idUsuarioPropietario INT     NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE MascotaTipo
(
  id          INT NOT NULL,
  nombre          NULL    ,
  descripcion     NULL    ,
  PRIMARY KEY (id)
);

CREATE TABLE PuntuacionServicio
(
  id                INT      NOT NULL,
  puntaje           int      NULL     COMMENT '0 a 10',
  descripcion       VARCHAR  NULL    ,
  fecha             DATETIME NULL    ,
  idReservaServicio INT      NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE ReservaDeServicio
(
  id               INT  NOT NULL,
  concretada       BOOL NOT NULL DEFAULT falso,
  idDisponibilidad INT  NOT NULL,
  idMascota        INT  NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE ServicioOfrecido
(
  id         INT NOT NULL,
  idUsuario  INT NOT NULL,
  idServicio INT NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE ServicioSoportado
(
  id          INT     NOT NULL,
  nombre      VARCHAR NOT NULL,
  descripcion VARCHAR NULL    ,
  PRIMARY KEY (id)
);

CREATE TABLE Usuario
(
  id        INT      NOT NULL,
  username  VARCHAR  NOT NULL,
  password  VARCHAR  NOT NULL,
  firstName VARCHAR  NOT NULL,
  lastName  VARCHAR  NOT NULL,
  birthDate DATETIME NOT NULL,
  telephone VARCHAR  NOT NULL,
  email     VARCHAR  NOT NULL,
  PRIMARY KEY (id)
);

ALTER TABLE Domicilio
  ADD CONSTRAINT FK_Usuario_TO_Domicilio
    FOREIGN KEY (idUsuario)
    REFERENCES Usuario (id);

ALTER TABLE ServicioOfrecido
  ADD CONSTRAINT FK_Usuario_TO_ServicioOfrecido
    FOREIGN KEY (idUsuario)
    REFERENCES Usuario (id);

ALTER TABLE ServicioOfrecido
  ADD CONSTRAINT FK_ServicioSoportado_TO_ServicioOfrecido
    FOREIGN KEY (idServicio)
    REFERENCES ServicioSoportado (id);

ALTER TABLE Disponibilidad
  ADD CONSTRAINT FK_MascotaTipo_TO_Disponibilidad
    FOREIGN KEY (idTipoMascota)
    REFERENCES MascotaTipo (id);

ALTER TABLE Disponibilidad
  ADD CONSTRAINT FK_ServicioOfrecido_TO_Disponibilidad
    FOREIGN KEY (idServicioOfrecido)
    REFERENCES ServicioOfrecido (id);

ALTER TABLE ReservaDeServicio
  ADD CONSTRAINT FK_Disponibilidad_TO_ReservaDeServicio
    FOREIGN KEY (idDisponibilidad)
    REFERENCES Disponibilidad (id);

ALTER TABLE Mascota
  ADD CONSTRAINT FK_Usuario_TO_Mascota
    FOREIGN KEY (idUsuarioPropietario)
    REFERENCES Usuario (id);

ALTER TABLE ReservaDeServicio
  ADD CONSTRAINT FK_Mascota_TO_ReservaDeServicio
    FOREIGN KEY (idMascota)
    REFERENCES Mascota (id);

ALTER TABLE PuntuacionServicio
  ADD CONSTRAINT FK_ReservaDeServicio_TO_PuntuacionServicio
    FOREIGN KEY (idReservaServicio)
    REFERENCES ReservaDeServicio (id);