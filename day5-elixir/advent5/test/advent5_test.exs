defmodule Advent5Test do
  use ExUnit.Case
  doctest Advent5

  test "the truth" do
    assert Advent5.password("abc") == "18f47a30"
  end
end
