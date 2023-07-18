input.onButtonPressed(Button.A, function () {
    music.play(music.tonePlayable(notas[notaParaTocar], music.beat(BeatFraction.Double)), music.PlaybackMode.UntilDone)
    basic.showNumber(notaParaTocar)
    notaParaTocar += 1
})
input.onButtonPressed(Button.B, function () {
    notaParaTocar = 0
    basic.clearScreen()
})
let notaParaTocar = 0
let notas: number[] = []
notas = [262, 294, 330]
notaParaTocar = 0
