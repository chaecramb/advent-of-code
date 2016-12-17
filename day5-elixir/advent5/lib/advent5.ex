defmodule Advent5 do
  def generate_password(door_id) do
    generate_password(door_id, 0, "", 8)
  end

  defp generate_password(_, _, password, 0), do: String.downcase(password)
  defp generate_password(door_id, index, password, remaining) do
    hash = md5_hash(door_id <> Integer.to_string(index))

    case next_char(hash) do
      "" -> 
        generate_password(door_id, index + 1, password, remaining)
      char -> 
        generate_password(door_id, index + 1, password <> char, remaining - 1)
    end
  end

  defp next_char(hash) do
    if Regex.match?(~r/^00000/, hash), do: String.at(hash, 5), else: ""
  end

  defp md5_hash(input) do
    :crypto.hash(:md5, input)
    |> Base.encode16
  end

  def main([door_id]) do
    IO.puts generate_password(door_id)
  end
end

