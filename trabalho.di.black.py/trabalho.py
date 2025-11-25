import flet as ft

def main(page: ft.Page):
    page.title = "Dark Watch"
    page.bgcolor = ft.Colors.BLACK
    page.scroll = ft.ScrollMode.AUTO

    # Dados de cada relógio
    watches = [
        {
            "nome": "Relógio Clássico Prata",
            "preco": "R$ 500,00",
            "descricao": "Estilo atemporal com mostrador prateado e pulseira de aço inoxidável.",
            "detalhes": "Material: Aço inoxidável\nMovimento: Analógico\nResistência à água: 5 ATM",
            "imagem": "https://static.netshoes.com.br/produtos/relogio-masculino-de-pulso-com-ponteiro-prata-moderno/06/67E-0960-006/67E-0960-006_zoom1.jpg?ts=1701134293",
        },
        {
            "nome": "Relógio Vintage Couro",
            "preco": "R$ 420,00",
            "descricao": "Design retrô com pulseira de couro legítimo, ideal para um visual elegante.",
            "detalhes": "Material: Couro legítimo\nMovimento: Analógico\nGarantia: 1 ano",
            "imagem": "https://a-static.mlcdn.com.br/800x560/relogio-de-ponteiros-masculino-de-pulso-vintage-jj95/jj95acessorios/10ureee015/65f485f90ba034f3d9aaa7d9d2bf0f86.jpeg",
        },
        {
            "nome": "Relógio Moderno Azul",
            "preco": "R$ 550,00",
            "descricao": "Pulseira azul e detalhes metálicos em um visual sofisticado e moderno.",
            "detalhes": "Material: Aço escovado\nMovimento: Analógico\nDisplay Luminoso: Sim",
            "imagem": "https://a-static.mlcdn.com.br/800x560/relogio-de-ponteiros-masculino-de-pulso-vintage-shaarms/jj95acessorios/9reee030/6b83ad6cd4647c4c0b2edb2eb3606aae.jpeg",
        },
    ]

    # Elementos mutáveis
    main_image = ft.Image(
        src=watches[0]["imagem"],
        fit=ft.ImageFit.CONTAIN,
        border_radius=ft.border_radius.all(15),
    )

    nome = ft.Text(watches[0]["nome"], color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD, size=30)
    preco = ft.Text(watches[0]["preco"], color=ft.Colors.WHITE, size=28, weight=ft.FontWeight.BOLD)
    descricao = ft.Text(watches[0]["descricao"], color=ft.Colors.GREY_300)
    detalhes = ft.Text(watches[0]["detalhes"], color=ft.Colors.GREY_300)

    # Função de mudança de relógio
    def change_watch(e, index):
        for i, elem in enumerate(options.controls):
            elem.opacity = 1 if i == index else 0.5
            elem.bgcolor = ft.Colors.AMBER_100 if i == index else ft.Colors.with_opacity(0.05, ft.Colors.WHITE)
        main_image.src = watches[index]["imagem"]
        nome.value = watches[index]["nome"]
        preco.value = watches[index]["preco"]
        descricao.value = watches[index]["descricao"]
        detalhes.value = watches[index]["detalhes"]

        # Atualiza com animação suave
        main_image.scale = 0.9
        main_image.update()
        page.update()
        main_image.scale = 1
        main_image.update()

        options.update()
        nome.update()
        preco.update()
        descricao.update()
        detalhes.update()

    # Miniaturas dinâmicas
    options = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
        controls=[
            ft.Container(
                content=ft.Image(src=w["imagem"], width=80, height=80, fit=ft.ImageFit.CONTAIN),
                width=85,
                height=85,
                border_radius=ft.border_radius.all(10),
                bgcolor=ft.Colors.AMBER_100 if i == 0 else ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
                opacity=1 if i == 0 else 0.5,
                on_click=lambda e, idx=i: change_watch(e, idx),
            )
            for i, w in enumerate(watches)
        ],
    )

    # Área da imagem principal
    product_images = ft.Container(
        col={'xs': 12, 'md': 6},
        bgcolor=ft.Colors.WHITE,
        padding=ft.padding.all(20),
        border_radius=ft.border_radius.all(20),
        shadow=ft.BoxShadow(blur_radius=10, color=ft.Colors.with_opacity(0.4, ft.Colors.BLACK)),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                main_image,
                ft.Divider(height=15, color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK)),
                options,
            ],
        ),
    )

    # Detalhes do produto
    product_details = ft.Container(
        col={'xs': 12, 'md': 6},
        padding=ft.padding.all(30),
        bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.GREY_900),
        border_radius=ft.border_radius.all(20),
        shadow=ft.BoxShadow(blur_radius=10, color=ft.Colors.with_opacity(0.4, ft.Colors.BLACK)),
        content=ft.Column(
            spacing=15,
            controls=[
                ft.Text("RELOGIOS", color=ft.Colors.AMBER, weight=ft.FontWeight.BOLD),
                nome,
                ft.Text("Pulso Para Mão", color=ft.Colors.GREY, italic=True),
                preco,
                ft.Row(
                    alignment=ft.MainAxisAlignment.START,
                    spacing=2,
                    controls=[
                        ft.Icon(name=ft.Icons.STAR, color=ft.Colors.AMBER if i < 4 else ft.Colors.GREY)
                        for i in range(5)
                    ],
                ),
                ft.Tabs(
                    selected_index=0,
                    height=150,
                    indicator_color=ft.Colors.AMBER,
                    label_color=ft.Colors.AMBER,
                    unselected_label_color=ft.Colors.GREY,
                    tabs=[
                        ft.Tab(text="Descrição", content=descricao),
                        ft.Tab(text="Detalhes", content=detalhes),
                    ],
                ),
                ft.ResponsiveRow(
                    controls=[
                        ft.Dropdown(
                            col=6,
                            label="Cor",
                            label_style=ft.TextStyle(color=ft.Colors.WHITE, size=16),
                            options=[
                                ft.dropdown.Option("Prata"),
                                ft.dropdown.Option("Preto"),
                                ft.dropdown.Option("Azul"),
                            ],
                        ),
                        ft.Dropdown(
                            col=6,
                            label="Quantidade",
                            label_style=ft.TextStyle(color=ft.Colors.WHITE, size=16),
                            options=[
                                ft.dropdown.Option(f"{num} unid") for num in range(1, 11)
                            ],
                        ),
                    ]
                ),
                ft.ElevatedButton(
                    text="Adicionar à Lista de Desejos",
                    style=ft.ButtonStyle(
                        padding=20,
                        bgcolor=ft.Colors.AMBER,
                        color=ft.Colors.BLACK,
                        shape=ft.RoundedRectangleBorder(radius=12),
                    ),
                ),
            ]
        ),
    )

    # Layout principal
    layout = ft.Container(
        width=1100,
        margin=30,
        content=ft.ResponsiveRow(
            columns=12,
            spacing=20,
            controls=[product_images, product_details],
        ),
    )

    page.add(layout)

ft.app(target=main)
