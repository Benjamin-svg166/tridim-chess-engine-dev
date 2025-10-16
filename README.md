👉 [Visit the engine codebase](https://github.com/Benjamin-svg166/tridim-chess=engine-spec)
### 🧠 Architecture Overview

| Module                | Role                                                   |
|-----------------------|--------------------------------------------------------|
| `BoardManager`        | Manages 3D board structure and piece placement         |
| `Piece`               | Unified object model for all chess pieces              |
| `PieceLogicEngine`    | Validates movement rules across layers                 |
| `GameStateTracker`    | Tracks turn order, move history, and snapshots         |
| `MoveExecutor`        | Executes moves and updates game state                  |
| `SpecialMoveHandler`  | Handles castling, en passant, and promotion            |
| `PositionEvaluator`   | Scores board states for AI overlays and drills         |
| `TacticalDrillBuilder`| Generates puzzles and Layered Zugzwang setups          |
| `OverlayRenderer`     | Visualizes threats and control zones                   |
| `UndoRedoManager`     | Enables alternate line navigation and rewinds          |
| `CoreEngine`          | Central coordinator connecting all modules             |
