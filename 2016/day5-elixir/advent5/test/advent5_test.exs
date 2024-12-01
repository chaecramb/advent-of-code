defmodule Advent5Test do
  use ExUnit.Case
  doctest Advent5

  test "example" do
    assert Advent5.generate_password("abc") == "18f47a30"
  end
end
