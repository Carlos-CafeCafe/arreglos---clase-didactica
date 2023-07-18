def on_button_pressed_a():
    global notaParaTocar
    music.play(music.tone_playable(notas[notaParaTocar], music.beat(BeatFraction.DOUBLE)),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_number(notaParaTocar)
    notaParaTocar += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global notaParaTocar
    notaParaTocar = 0
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

notaParaTocar = 0
notas: List[number] = []
notas = [262, 294, 330]
notaParaTocar = 0