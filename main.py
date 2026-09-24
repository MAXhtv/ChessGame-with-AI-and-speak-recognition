import chess    
import Chessgame as Chess
import speech_recognition as sr
import pyaudio

def listening():
    print("enter 'b' to speak")
    while True:
        answ=input(": ")
        if answ=="b":
            mic=sr.Recognizer()
            with sr.Microphone() as source:
                mic.adjust_for_ambient_noise(source)
                print("listening... ")
                audio=mic.listen(source)
            try:
                phrase=mic.recognize_google(audio, language="pt-BR")
                print(phrase)
                return phrase.replace(" ", "").lower()
            except sr.UnknownValueError:
                print('error')
            except sr.RequestError as e:
                print(e)

def playChess():
    while not Chess.board.is_game_over():
        print("\n")
        print(Chess.board.unicode())
        print("\n")

        print("Turn:", Chess.board.turn)
        #movementPlayer=input("Put your moviment here (ex:e2e4): ")
        print("your movement here (ex:e2e4): ")
        movementPlayer=listening()
        try:
            movement=chess.Move.from_uci(movementPlayer)
            if movement not in Chess.board.legal_moves:
                print("invalid movement")
                continue
            Chess.board.push(movement)
        
            if Chess.board.is_game_over():
                break
            AIMove=Chess.selectNextMove(3)
            print("AI played", AIMove)
            Chess.board.push(AIMove)
        except:
            print("invalid format")

playChess()