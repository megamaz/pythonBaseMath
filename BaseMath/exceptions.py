class DefaultBaseException(Exception):
    """The default Base Math exception."""


class BaseDoesNotMatchError(DefaultBaseException):
    """Gets raised when trying to do math on two numbers with different bases."""

class BaseOutOfRange(DefaultBaseException):
    """Gets raised when the given base is > 36 or < 2"""

class NumberOutOfBaseRange(DefaultBaseException):
    """Gets raised when trying to do math with a number that is above the Symbol's base"""

class CannotDivideSymbols(DefaultBaseException):
    """Gets raised when trying to divide two symbols together."""

class IncorrectExpression(DefaultBaseException):
    """Gets raied when an expression is incorrect and causes an error."""

class CannotCompareDifferingBases(DefaultBaseException):
    """Gets raised when trying to compare two numbers with differing bases."""