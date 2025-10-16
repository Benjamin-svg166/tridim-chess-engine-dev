# engine/core_engine.py

from engine.board_manager import BoardManager
from engine.piece_logic_engine import PieceLogicEngine
from engine.move_executor import MoveExecutor
from engine.game_state_tracker import GameStateTracker
from engine.special_move_handler import SpecialMoveHandler
from engine.position_evaluator import PositionEvaluator
from engine.tactical_drill_builder import TacticalDrillBuilder
from engine.overlay_renderer import OverlayRenderer
from engine.undo_redo_manager import UndoRedoManager

class CoreEngine:
    """
    Central coordinator for tridimensional chess engine.
    Connects all modules for simulation, training, and cognition.
    """

    def __init__(self):
        self.board = BoardManager()
        self.tracker = GameStateTracker()
        self.logic = PieceLogicEngine(self.board)
        self.executor = MoveExecutor(self.board)
        self.specials = SpecialMoveHandler(self.board, self.tracker)
        self.evaluator = PositionEvaluator(self.board)
        self.drills = TacticalDrillBuilder(self.board, self.logic)
        self.renderer = OverlayRenderer(self.board, self.logic)
        self.undo_redo = UndoRedoManager(self.tracker, self.board)

    def simulate_drill(self, theme="zugzwang"):
        drill = self.drills.generate_drill(theme)
        print("Setup:", drill["setup"])
        print("Solution:", drill["solution"])
