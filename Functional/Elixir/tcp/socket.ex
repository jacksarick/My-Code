defmodule Socket do
	def start(port) do
		tcp_options = [:binary, packet: :line, active: false, reuseaddr: true]
		{:ok, socket} = :gen_tcp.listen(port, tcp_options)
		listen(socket)
	end

	defp listen(socket) do
		{:ok, conn} = :gen_tcp.accept(socket)
		spawn(fn -> recv(conn) end)
		listen(socket)
	end

	defp recv(conn) do
		case :gen_tcp.recv(conn, 0) do
			{:ok, data} -> send(conn, data)
			{:error, :closed} -> :ok
		end
	end

	defp senv(conn, msg) do
		:gen_tcp.send(conn, msg)
		recv(conn)
	end
end

Socket.start(6000)