from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

config.frame_size = (1080,1920) #(270,480) 
config.frame_width = 128/9 # 128/9

## Compilar com: manim -p video02.py --disable_caching
pular_animacao = False
er = .2
class Video(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="pt", tld="com"))
        
        COR_FUNDO = rgb_to_color(np.array([0.875,0.812,0.761]))
        self.camera.background_color = COR_FUNDO

        ############### NOVA SEÇÂO
        self.next_section("Abertura",
                          skip_animations = pular_animacao)

        formula = MathTex(r'x=\dfrac{-b\pm \sqrt{b^2-4ac}}{2a}',
                          font_size=48, color = BLACK)

        titulo_video = Tex("Resolvendo Equações do 2º Grau", font_size = 72,
                           color = PURE_BLUE)
        sub_video = Tex("Fórmula de Bhaskara",
                              font_size = 48, color = BLUE_E)
        autor = Tex("Prof. Douglas", font_size = 48,
                    tex_template=TexFontTemplates.french_cursive,
                    color = BLUE_E)
        
        titulo_capa = VGroup(titulo_video,
                             sub_video).arrange_in_grid(cols=1)
        
        self.add(titulo_capa.shift(5*UP))
        self.add(autor.shift(10*UP))

        self.wait(.5)   # Tá..., mas você já usou a fórmula de Bháskara hoje?!
        with self.voiceover(text="Você já usou a fórmula de Bhaskara hoje?!") as tracker:
            self.play(Write(formula), run_time=tracker.duration)

        self.wait(.5)
        with self.voiceover(text='Vem comigo e vamos relembrar como aplicá-la!') as tracker:
            self.play(Unwrite(formula), FadeOut(titulo_capa,autor), 
                      run_time = tracker.duration)

        self.wait()
        
        ## Enunciado
        ################ NOVA SEÇÂO
        self.next_section("Enunciado",
                          skip_animations=False)
        titulo = Title(r'Resolva a equação', include_underline = False,
                       color = PURE_BLUE)
        linha_abaixo = Line(LEFT,RIGHT, color = PURE_BLUE)
        linha_abaixo.next_to(titulo,DOWN, buff=.25)
        linha_abaixo.width = config["frame_width"]-5

        with self.voiceover("Vamos resolver juntos a equação ") as tracker:
            self.play(Write(titulo.shift(8*UP)),Create(linha_abaixo.shift(7*UP)))

        enunciado_eq = MathTex(r'{{x^2}} - 4{{x}} + 3 {{=}}0', font_size = 72, color = BLACK)
        enunciado_eq.shift(8*UP)

        with self.voiceover("Xis ao quadrado menos quatro xis mais três igual a zero.") as tracker:
            self.play(Write(enunciado_eq), run_time = tracker.duration)

        
        with self.voiceover(text="Trata-se mesmo de uma equação de segundo grau") as tracker:
            self.wait(tracker.duration+er)

        ind_eq_enum = Indicate(enunciado_eq[0], scale_factor = 2, color = PURE_BLUE)
        with self.voiceover(text="pois a maior potência de xis que aparece está em xis ao quadrado"
        ) as tracker:
            self.wait(.5*tracker.duration)
            self.play(ind_eq_enum, run_time = .5*tracker.duration)
        

        coef_a1 = MathTex('1', font_size = 72, color = RED).next_to(enunciado_eq[0],LEFT)
        y = enunciado_eq.get_bottom() - coef_a1.get_bottom()
        coef_a1.shift(np.array([-.1,y[1],0]))
        coef_b1 = enunciado_eq[1].copy()
        coef_b1.set(color = RED)
        coef_c1 = enunciado_eq[3].copy()
        coef_c1.set(color = RED)

        coeficientes = VGroup(MathTex('a={{1}}',font_size = 60, color = BLACK),
                              MathTex('b={{-4}}',font_size = 60, color = BLACK),
                              MathTex('c={{3}}',font_size = 60, color = BLACK)).arrange_in_grid(rows=1,buff=2)
        
        coeficientes.next_to(enunciado_eq,DOWN).shift(.5*DOWN)

        with self.voiceover("Para aplicar a fórmula precisamos garantir que a equação esteja neste formato, com o igual a zero.")as tracker:
            self.wait(.6*tracker.duration)
            self.play(Indicate(enunciado_eq[-2:], scale_factor=1.5,color=PURE_BLUE), run_time = .4*tracker.duration)

        self.wait(er)

        with self.voiceover("O primeiro passo é determinar os valores dos coeficientes a, b e c.")as tracker:
            self.wait(.6*tracker.duration)
            self.play(FadeIn(coeficientes[0][0]), run_time = .25)
            self.play(FadeIn(coeficientes[1][0]), run_time = .25)
            self.play(FadeIn(coeficientes[2][0]), run_time = .25)

        with self.voiceover("O coeficiente Ah é sempre aquele que acompanha o xis ao quadrado.") as tracker:
            self.wait(tracker.duration+er)
        
        with self.voiceover("Quando não há nada na frente da variável, o coeficiente é 1.") as tracker:
            self.wait(.7*tracker.duration)
            self.play(FadeIn(coef_a1), run_time = .5)

        with self.voiceover("Sendo assim, A é igual a 1.") as tracker:
            self.wait(.5*tracker.duration)
            self.play(Transform(coef_a1,coeficientes[0][1], run_time=.5*tracker.duration))

        with self.voiceover("Já o coeficiente B, é aquele que acompanha o termo com xis.") as tracker:
            self.wait(.5*tracker.duration)
            self.play(FadeIn(coef_b1), run_time = .5*tracker.duration)
        
        with self.voiceover("Neste caso, B é igual a -4") as tracker:
            self.wait(.5*tracker.duration)
            self.play(Transform(coef_b1,coeficientes[1][1], run_time = .5*tracker.duration))

        with self.voiceover("Perceba que na nossa equação o B é negativo, o sinal é muito importante.") as tracker:
            self.wait(tracker.duration+er)

        self.wait(er)

        with self.voiceover("O coeficiente C é o termo independente, ou seja, aquele que está sozinho, sem o xis.") as tracker:
            self.wait(.5*tracker.duration)
            self.play(FadeIn(coef_c1), run_time = .5*tracker.duration)

        with self.voiceover("Na nossa equação o C vale 3:") as tracker:
            self.wait(.5*tracker.duration)
            self.play(coef_c1.animate.shift(coeficientes[2][1].get_center()-coef_c1.get_center()+.2*RIGHT),
                                            run_time = .5*tracker.duration)

        with self.voiceover("Quando o coeficiente for positivo, aconselho não carregar o sinal.") as tracker:
            self.wait(.5*tracker.duration)
            self.play(Transform(coef_c1,coeficientes[2][1]), run_time = .5*tracker.duration)

        self.remove(coef_a1,coef_b1,coef_c1,coeficientes[0][0],coeficientes[1][0],coeficientes[2][0],coeficientes[0][1],coeficientes[1][1],coeficientes[2][1])
        self.add(coeficientes[0],coeficientes[1],coeficientes[2])

        #### Equações

        calculo_delta = VGroup(MathTex(r'\Delta = {{b^2 - 4ac}}', font_size = 60, color = BLACK),
                               MathTex(r'\Delta = {{(-4)^2}} - 4\times {{ 1 }} \times {{3}}', font_size = 60, color = BLACK),
                               MathTex(r'\Delta = {{16}}-12', font_size = 60, color = BLACK),
                               MathTex(r'\Delta = {{4}}', font_size = 60, color = BLACK)).arrange_in_grid(cols=1,buff=.75)
        
        for i in range(len(calculo_delta)):
            y = calculo_delta[1].get_left()-calculo_delta[i].get_left()
            calculo_delta[i].shift(np.array([y[0],0,0]))

        calculo_x = VGroup(MathTex(r'x = \dfrac{-b\pm \sqrt{\Delta}}{2a}', font_size = 60, color = BLACK),
                           MathTex(r'x = \dfrac{-(-4)\pm\sqrt{4}}{2\times  1 }', font_size = 60, color = BLACK),
                           MathTex(r'x = \dfrac{ 4\pm 2 }{ 2 }', font_size = 60, color = BLACK)).arrange_in_grid(cols=1,buff=.75)

        for i in range(len(calculo_x)):
            y = calculo_x[1].get_left()-calculo_x[i].get_left()
            calculo_x[i].shift(np.array([y[0],0,0]))

        contas = VGroup(calculo_delta,calculo_x).arrange_in_grid(rows=1,buff=1)
        contas.next_to(coeficientes,DOWN).shift(.5*DOWN)

        calculo_final = VGroup(MathTex(r"x' = \dfrac{4 + 2}{2} = \dfrac{6}{2} = 3", font_size = 60, color = BLACK),
                          MathTex(r"x'' = \dfrac{4 - 2}{2} = \dfrac{2}{2} = 1", font_size = 60, color = BLACK)).arrange_in_grid(cols=1,buff=1)

        calculo_final.next_to(contas,DOWN).shift(DOWN)

        solucao = MathTex(r'S = \{\,1\,,\,3\,\}', font_size = 60, color = BLACK).next_to(calculo_final,DOWN)
        solucao.shift(DOWN)

        with self.voiceover("O próximo passo é calcular o discriminante da equação, ele é representado pela letra grega Delta maiúsculo ") as tracker:
            self.wait(.7*tracker.duration)
            self.play(Write(calculo_delta[0][0]), run_time = .2*tracker.duration)

        with self.voiceover("O valor do Delta é igual a B ao quadrado menos quatro Ah vezes C") as tracker:
            self.wait(.2*tracker.duration)
            self.play(Write(calculo_delta[0][1]), run_time = .7*tracker.duration)

        with self.voiceover("Substituímos os valores na expressão:") as tracker:
            self.wait(.5*tracker.duration)
            self.play(Write(calculo_delta[1][0]), run_time = .5)
        
        with self.voiceover("B vale menos quatro e, por isso, o parênteses é obrigatório:") as tracker:
            aux = coeficientes[1].copy()
            self.remove(coeficientes[1],coef_b1)
            self.add(aux)
            self.play(Indicate(aux,scale_factor=1.5, color = PURE_BLUE), run_time = .5*tracker.duration)
            self.add(coeficientes[1])
            self.play(Transform(aux,calculo_delta[1][1]), run_time = .5*tracker.duration)
            self.add(calculo_delta[1][1])
            self.remove(aux)

        with self.voiceover("copiamos o menos quatro da fórmula") as tracker:
            self.wait(.5*tracker.duration)
            self.play(Write(calculo_delta[1][2]), run_time = .5*tracker.duration)

        with self.voiceover("Ah é igual a um e sendo positivo não precisa do parênteses") as tracker:
            aux = coeficientes[0].copy()
            self.add(aux)
            self.remove(coeficientes[0],coef_a1)
            self.play(Indicate(aux,scale_factor=1.5, color = PURE_BLUE), run_time = .5*tracker.duration)
            self.add(coeficientes[0])
            self.play(Transform(aux,calculo_delta[1][3]), run_time = .4*tracker.duration)
            self.add(calculo_delta[1][3])
            self.remove(aux)

        with self.voiceover("e o coeficiente C é igual a três e também dispensa parênteses") as tracker:
            aux = coeficientes[2].copy()
            self.add(aux)
            self.remove(coeficientes[2])
            aux_trans = Indicate(aux,scale_factor=1.5, color = PURE_BLUE)
            self.play(aux_trans, run_time = .5*tracker.duration)
            self.add(coeficientes[2])
            self.play(Transform(aux,calculo_delta[1][4:]), run_time = .4*tracker.duration)
            self.add(calculo_delta[1][4:])
            self.remove(aux)

        self.play(Write(calculo_delta[2][0]), run_time = .5)

        with self.voiceover("primeiro desenvolvemos o quadrado do quatro negativo que é igual a dezesseis:") as tracker:
            self.play(Indicate(calculo_delta[1][1],scale_factor=1.5, color = PURE_BLUE), run_time = .5*tracker.duration)
            aux = calculo_delta[1][1].copy()
            self.add(aux)
            self.play(Transform(aux,calculo_delta[2][1]))
            self.add(calculo_delta[2][1])
            self.remove(aux)

        with self.voiceover("podemos calcular também quatro vezes um vezes três, obtendo o produto doze") as tracker:
            self.play(Indicate(calculo_delta[1][2:], scale_factor=1.5, color = PURE_BLUE), run_time = .5*tracker.duration)
            aux = calculo_delta[1][2:].copy()
            self.add(aux)
            self.play(Transform(aux,calculo_delta[2][2]))
            self.add(calculo_delta[2][2])
            self.remove(aux)

        with self.voiceover("Se houvesse número negativo neste último produto, aplicaríamos as regras de sinais") as tracker:
            self.wait(tracker.duration+er)

        def Transformar(mob_source, mob_target,time):
            self.play(Indicate(mob_source,scale_factor = 1.5, color = PURE_BLUE), run_time = .5*time)
            aux = mob_source.copy()
            self.add(aux)
            self.play(Transform(aux,mob_target), run_time = .5*time)
            self.add(mob_target)
            self.remove(aux)
        
        with self.voiceover("Dezesseis menos doze é igual a quatro.") as tracker:
            self.play(Write(calculo_delta[3][0]), run_time = .5*tracker.duration)
            Transformar(calculo_delta[2][1:],calculo_delta[3][1],.5*tracker.duration)

        with self.voiceover("Portanto o Delta é igual a quatro.") as tracker:
            self.wait(.5*tracker.duration)
            self.play(Indicate(calculo_delta[3], scale_factor=1.5, color = PURE_BLUE), run_time = .5*tracker.duration)

        with self.voiceover("Agora vamos para a segunda parte da fórmula. Muitos preferem fazer os dois cálculos juntos, mas eu gosto de fazer separado.") as tracker:
            self.play(Write(calculo_x[0]), run_time = .5*tracker.duration)
            self.play(FadeIn(*[calculo_x[1][0][i] for i in [0,1,2,7,8,9,11,12,13] ]), run_time = .5*tracker.duration)
        
        with self.voiceover("Primeiro substituímos B por menos quatro, lembrando de colocar os parênteses.") as tracker:
            Transformar(coeficientes[1],calculo_x[1][0][4:6], .5*tracker.duration)
            self.play(FadeIn(calculo_x[1][0][3],calculo_x[1][0][6]), run_time = .4*tracker.duration)

        with self.voiceover("Substituímos o Delta por quatro") as tracker:
            Transformar(calculo_delta[3], calculo_x[1][0][10], tracker.duration)

        with self.voiceover("e substituímos o Ah por um:") as tracker:
            Transformar(coeficientes[0],calculo_x[1][0][14],tracker.duration)

        with self.voiceover("Prosseguimos com cálculo:") as tracker:
            self.wait(tracker.duration+er)

        with self.voiceover("Primeiro aplicamos a regra de sinal, de modo que xis é igual a quatro") as tracker:
            self.play(FadeIn(*[ calculo_x[2][0][i] for i in [0,1,3,5] ]), run_time = .4*tracker.duration)
            Transformar(calculo_x[1][0][2:7], calculo_x[2][0][2], .6*tracker.duration)
        
        with self.voiceover("mais ou menos raiz de quatro que é igual a dois") as tracker:
            Transformar(calculo_x[1][0][8:11],calculo_x[2][0][4],.6*tracker.duration)
        
        with self.voiceover("Dividido por dois vezes um que é igual a dois") as tracker:
            Transformar(calculo_x[1][0][12:],calculo_x[2][0][6], .8*tracker.duration)

        aux1 = VGroup(*[ calculo_x[2][0][i].copy() for i in [0,1,2,4,5,6] ])
        aux2 = VGroup(*[ calculo_x[2][0][i].copy() for i in [0,1,2,4,5,6] ])
        self.add(aux1,aux2)
        aux3 = VGroup(*[ calculo_final[0][0][i] for i in [0,1,2,3,5,6,7] ])
        aux4 = VGroup(*[ calculo_final[1][0][i] for i in [0,1,2,3,4,6,7,8] ])
        with self.voiceover("Agora chegou o momento de separarmos o cálculo de xis linha e xis duas linhas: ") as tracker:
            self.wait(.5*tracker.duration)
            self.play(Transform(aux1,aux3),Transform(aux2,aux4), run_time = .5*tracker.duration)

        with self.voiceover("xis linha fica com o sinal positivo") as tracker:
            Transformar(calculo_x[2][0][3],calculo_final[0][0][4], .8*tracker.duration)
            
        with self.voiceover("e xis duas linhas fica com o sinal negativo.") as tracker:
            Transformar(calculo_x[2][0][3],calculo_final[1][0][5], .8*tracker.duration)
        
        self.add(calculo_final[0][0][:8],calculo_final[1][0][:9])
        self.remove(aux1,aux2,aux3,aux4)

        self.wait(er)

        with self.voiceover("Agora é só finalizar ") as tracker:
            self.wait(tracker.duration+er)

        with self.voiceover("Xis linha é igual a seis sobre dois") as tracker:
            self.play(FadeIn(calculo_final[0][0][8],calculo_final[0][0][10:12]), run_time=.3*tracker.duration)
            Transformar(calculo_final[0][0][3:6],calculo_final[0][0][9],.7*tracker.duration)
        
        with self.voiceover("Logo, xis linha é igual a três") as tracker:
            self.play(FadeIn(calculo_final[0][0][12]), run_time=.3*tracker.duration)
            Transformar(calculo_final[0][0][9:12],calculo_final[0][0][13],.7*tracker.duration)

        with self.voiceover("e Xis duas linhas é igual a dois sobre dois") as tracker:
            self.play(FadeIn(calculo_final[1][0][9],calculo_final[1][0][11:13]), run_time=.3*tracker.duration)
            Transformar(calculo_final[1][0][4:7],calculo_final[1][0][10],.7*tracker.duration)
        
        with self.voiceover("Assim, xis duas linhas é igual a um.") as tracker:
            self.play(FadeIn(calculo_final[1][0][13]), run_time=.3*tracker.duration)
            Transformar(calculo_final[1][0][10:13],calculo_final[1][0][14],.7*tracker.duration)

        with self.voiceover("Finalmente, podemos escrever nosso conjunto solução S") as tracker:
            self.wait(.5*tracker.duration)
            self.play(FadeIn(solucao[0][:3],solucao[0][4],solucao[0][6]))

        with self.voiceover("a partir das duas soluções: xis linha") as tracker:
            self.wait(.5*tracker.duration)
            Transformar(calculo_final[0][0][-1],solucao[0][5],.5*tracker.duration)

        with self.voiceover("e xis duas linhas") as tracker:
            Transformar(calculo_final[1][0][-1],solucao[0][3],.5*tracker.duration)

        with self.voiceover("Os professores de matemática gostam quando escrevemos as soluções dentro do conjunto solução na ordem crescente.") as tracker:
            self.wait(tracker.duration+er)

        self.wait(er)

        with self.voiceover("Responda para mim nos comentários") as tracker:
            self.wait(tracker.duration)