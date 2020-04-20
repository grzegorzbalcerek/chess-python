from color import Color
from figure import Figure, FigureType
from field import Field

def starting_board():
    return {
        (1,1): Figure(FigureType.Rook, Color.White),
        (2,1): Figure(FigureType.Knight, Color.White),
        (3,1): Figure(FigureType.Bishop, Color.White),
        (4,1): Figure(FigureType.Queen, Color.White),
        (5,1): Figure(FigureType.King, Color.White),
        (6,1): Figure(FigureType.Bishop, Color.White),
        (7,1): Figure(FigureType.Knight, Color.White),
        (8,1): Figure(FigureType.Rook, Color.White),
        (1,2): Figure(FigureType.Pawn, Color.White),
        (2,2): Figure(FigureType.Pawn, Color.White),
        (3,2): Figure(FigureType.Pawn, Color.White),
        (4,2): Figure(FigureType.Pawn, Color.White),
        (5,2): Figure(FigureType.Pawn, Color.White),
        (6,2): Figure(FigureType.Pawn, Color.White),
        (7,2): Figure(FigureType.Pawn, Color.White),
        (8,2): Figure(FigureType.Pawn, Color.White),
        (1,7): Figure(FigureType.Pawn, Color.Black),
        (2,7): Figure(FigureType.Pawn, Color.Black),
        (3,7): Figure(FigureType.Pawn, Color.Black),
        (4,7): Figure(FigureType.Pawn, Color.Black),
        (5,7): Figure(FigureType.Pawn, Color.Black),
        (6,7): Figure(FigureType.Pawn, Color.Black),
        (7,7): Figure(FigureType.Pawn, Color.Black),
        (8,7): Figure(FigureType.Pawn, Color.Black),
        (1,8): Figure(FigureType.Rook, Color.Black),
        (2,8): Figure(FigureType.Knight, Color.Black),
        (3,8): Figure(FigureType.Bishop, Color.Black),
        (4,8): Figure(FigureType.Queen, Color.Black),
        (5,8): Figure(FigureType.King, Color.Black),
        (6,8): Figure(FigureType.Bishop, Color.Black),
        (7,8): Figure(FigureType.Knight, Color.Black),
        (8,8): Figure(FigureType.Rook, Color.Black)
    }

def show_board(board):
    """
    Shows the board.

    >>> print(show_board(starting_board()))
     abcdefgh
    8RNBQKBNR8
    7PPPPPPPP7
    6........6
    5........5
    4........4
    3........3
    2pppppppp2
    1rnbqkbnr1
     abcdefgh
    """
    def row_to_str(row):
        return "".join([str(board.get((col,row), ".")) for col in range(1,9)])
    return (" abcdefgh\n" +
        "".join([ (str(row) + row_to_str(row) + str(row) + "\n") for row in range(8,0,-1)]) +
        " abcdefgh")

if __name__ == "__main__":
    import doctest
    doctest.testmod()

#  /**
#    * Returns a new board, updated with a move.
#    */
#  def updateBoard(board: Board, move: Move): Board = move match {
#    case RegularMove(from,to) =>
#      board.get(from).fold(board)( figure =>
#        board - from + (to->figure))
#    case PromotionMove(from,to,figure) =>
#      board.get(from).fold(board)( _ =>
#        board - from + (to->figure))
#    case EnPassantMove(from,to,captured) =>
#      board.get(from).fold(board)( figure =>
#        board - from - captured + (to->figure))
#    case CastlingMove(from,to,rookFrom,rookTo) =>
#      (board.get(from), board.get(rookFrom)) match {
#        case (Some(figure),Some(rookFigure)) =>
#          board - from + (to->figure) - rookFrom + (rookTo->rookFigure)
#        case _ => board
#      }
#  }
#}
#
#showBoard(updateBoard(startingBoard,RegularMove(Field(2,2),Field(2,3))))
#showBoard(updateBoard(startingBoard,RegularMove(Field(3,3),Field(2,3))))
#showBoard(updateBoard(startingBoard,PromotionMove(Field(2,2),Field(2,8),Figure(Queen,White))))
#showBoard(updateBoard(startingBoard,EnPassantMove(Field(2,2),Field(3,3),Field(3,7))))
#showBoard(updateBoard(startingBoard,CastlingMove(Field(5,1),Field(3,1),Field(1,1),Field(4,1))))
