       *Functions in Cobol:
       * an experiment
       program-id. function-test.

       environment division.
       configuration section.

       data division.
       working-storage section.

       procedure division.
          create function duple (x int)
          returns integer
          deterministic
          return x*x;

          display function duple ( 12 )

       end program function-test.