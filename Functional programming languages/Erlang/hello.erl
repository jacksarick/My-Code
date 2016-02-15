-module(hello).
-export([start/0]). start() ->
	aio:format("Hello world~n").