# Ajedres 2024

# Trabajo de Juan Cruz Sacchi

# Como se instala el ajedrez

para instalar dockerfile:

- sudo apt install docker

para crear la imagen de docker en el juego de ajedrez:

- sudo docker buildx build --no-cache -t ajedrez_juancruzsacchi

para ejecutar los tests e iniciar el juego:

- sudo docker run -i ajedrez_juancruzsacchi

# Como se juega al ajedrez

La partida comienza con dos jugadores, cada uno con 16 piezas cada uno, por un lado un jugador tiene piezas de color BLANCO y el otro piezas de color NEGRO.

El jugador con las piezas BLANCAS es el que empieza la partida primero, cada pieza se mueve de una forma en especial y tiene su propia funcione durante la partida, y los jugadores tiene que saber como mover las piezas de la manera mas inteligente posible para acorralar al otro.

Para poder ganar uno de los jugadores tiene que capturar la pieza clave del otro, el REY, debe de acorralarlo con las otras piezas. 

Cuando el REY esta en una posicion en la que otra pieza lo puede capturar, el jugador esta obligado a mover al REY para que este seguro o mover otra pieza para cubrirlo.

Si el REY esta en una posicion comprometida se le llama JAQUE, y si es rodeado y no es capas de hacer ningun movimiento para escapar se le llama JAQUE MATE.

La partida termina una vez que el jugador le hace un JAQUE MATE al otro.

# Como se comprueban las reglas de las piezas

Para asegurar el buen funcionamiento del juego y movimiento correcto de las piezas, desarrolle el TEST para cada pieza del juego:

test_king.py

test_queen.py

test_rook.py

test_knight.py

test_bishop.py

test_pawn.py
