      *FizzBuzz in Cobol
        IDENTIFICATION DIVISION.
        PROGRAM-ID. FIZZBUZZ.

        DATA DIVISION.
          WORKING-STORAGE SECTION.
           01 WS-NUM PIC 9(2) VALUE 0.
           01 WS-MOD-THRE PIC 9.
           01 WS-MOD-FIVE PIC 9.

        PROCEDURE DIVISION.
          MAIN-PARA.
          PERFORM LOOP-PARA 20 TIMES.
          STOP RUN.
           
          LOOP-PARA.
          SET WS-NUM UP BY 1.
          COMPUTE WS-MOD-THRE = FUNCTION MOD ( WS-NUM, 3 ).
          COMPUTE WS-MOD-FIVE = FUNCTION MOD ( WS-NUM, 5 ).

          IF WS-MOD-THRE = 0 AND WS-MOD-FIVE = 0 THEN
            DISPLAY "FIZZBUZZ".

          IF WS-MOD-THRE = 0 THEN
            DISPLAY "FIZZ".

          IF WS-MOD-FIVE = 0 THEN
            DISPLAY "BUZZ".

          IF NOT WS-MOD-THRE = 0 AND NOT WS-MOD-FIVE = 0 THEN
            DISPLAY WS-NUM.

        STOP RUN.