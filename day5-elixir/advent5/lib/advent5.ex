defmodule Advent5 do
  def generate_password(door_id) do
    generate_password(door_id, 0, "")
  end

  defp generate_password(door_id, index, password) do
    if String.length(password) == 8 do
      password
    else
      IO.puts(password)
      IO.puts(index)
      hash = md5_hash(door_id <> Integer.to_string(index))

      relevant_section = String.slice(hash, 0..5)

      if String.slice(relevant_section, 0..4) == "00000" do
        next_char = String.last(relevant_section)
        generate_password(door_id, index + 1, password <> next_char)
      else 
        generate_password(door_id, index + 1, password)
      end
    end
  end

  defp md5_hash(input) do
    :crypto.hash(:md5, input)
    |> Base.encode16
  end
end
