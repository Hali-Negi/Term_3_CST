from resources.powerups import NormalPowerUp
from resources.powerups import FreezePowerUp, BombPowerUp
from resources.colors import Colors
from resources.tetrominos import (
    ZTetromino,
    JTetromino,
    TTetromino,
    LTetromino,
    STetromino,
    OTetromino,
    ITetromino,
)



class TetrominoFactory:

    def create_z(self):
        pass

    def create_j(self):
        pass

    def create_t(self):
        pass

    def create_l(self):
        pass

    def create_s(self):
        pass

    def create_o(self):
        pass

    def create_i(self):
        pass

class NormalFactory(TetrominoFactory):

    def create_z(self):
        return ZTetromino(NormalPowerUp())

    def create_j(self):
        return JTetromino(NormalPowerUp())

    def create_t(self):
        return TTetromino(NormalPowerUp())

    def create_l(self):
        return LTetromino(NormalPowerUp())

    def create_s(self):
        return STetromino(NormalPowerUp())

    def create_o(self):
        return OTetromino(NormalPowerUp())

    def create_i(self):
        return ITetromino(NormalPowerUp())


class FreezeFactory(TetrominoFactory):

    def create_z(self):
        return ZTetromino(FreezePowerUp())

    def create_j(self):
        return JTetromino(FreezePowerUp())

    def create_t(self):
        tetromino = TTetromino(FreezePowerUp())
        tetromino.color = Colors.ORANGE.value
        return tetromino

    def create_l(self):
        return LTetromino(FreezePowerUp())

    def create_s(self):
        return STetromino(FreezePowerUp())

    def create_o(self):
        return OTetromino(FreezePowerUp())

    def create_i(self):
        return ITetromino(FreezePowerUp())


class BombFactory(TetrominoFactory):

    def create_z(self):
        return ZTetromino(BombPowerUp())

    def create_j(self):
        return JTetromino(BombPowerUp())

    def create_t(self):
        tetromino = TTetromino(BombPowerUp())
        tetromino.color = (120, 0, 0)
        return tetromino

    def create_l(self):
        return LTetromino(BombPowerUp())

    def create_s(self):
        return STetromino(BombPowerUp())

    def create_o(self):
        return OTetromino(BombPowerUp())

    def create_i(self):
        return ITetromino(BombPowerUp())
