from flet import Page, AppBar, NavigationBar, NavigationBarDestination, MainAxisAlignment, View, Row, Column, Container, RouteChangeEvent, ViewPopEvent, ControlEvent, Text, ElevatedButton, app, colors, icons

def main(page: Page):
    page.title = "Test"
    page.vertical_alignment = MainAxisAlignment.CENTER

    def _add_text(e: ControlEvent) -> None:
        page.views[-1].controls.append(
            Row(
                controls=[
                    Column(
                        controls=[
                            Text("Add"),
                        ],
                    ),
                ],
            ),
        )
        page.update()

    def route_change(route: RouteChangeEvent) -> None:
        page.views.clear()
        if page.route == "/" or page.route == "/main" or page.route == "/main/home":
            page.views.append(
                View(
                    route="/",
                    appbar=AppBar(
                        title=Text("Main"),
                        bgcolor=colors.SURFACE_VARIANT,
                    ),
                    navigation_bar=nav,
                    controls=[
                        Row(
                            controls=[
                                Text("Main"),
                                Column(
                                    controls=[
                                        ElevatedButton(text="Next", on_click=lambda e: page.go("/main")),
                                        ElevatedButton(text="Press", on_click=lambda e: _add_text(e=e)),
                                    ],
                                    alignment=MainAxisAlignment.CENTER,
                                ),
                            ],
                            alignment=MainAxisAlignment.CENTER,
                        ),
                    ],
                ),
            )
        if page.route == "/main" or page.route == "/main/home":
            page.views.append(
                View(
                    route="/main",
                    appbar=AppBar(title=Text("Main"), bgcolor=colors.SURFACE_VARIANT),
                    navigation_bar=nav,
                    controls=[
                        Row(
                            controls=[
                                Text("Main"),
                                Column(
                                    controls=[
                                        ElevatedButton(text="Next", on_click=lambda e: page.go("/main/home")),
                                        ElevatedButton(text="Back", on_click=lambda e: page.go("/")),
                                        ElevatedButton(text="Press", on_click=lambda e: _add_text(e=e)),
                                    ],
                                    alignment=MainAxisAlignment.CENTER,
                                ),
                            ],
                            alignment=MainAxisAlignment.CENTER,
                        ),
                    ],
                ),
            )
        if page.route == "/main/home":
            page.views.append(
                View(
                    route="/main/home",
                    appbar=AppBar(title=Text("Home"), bgcolor=colors.SURFACE_VARIANT),
                    navigation_bar=nav,
                    controls=[
                        Row(
                            controls=[
                                Text("Main Home"),
                                Column(
                                    controls=[
                                        ElevatedButton(text="Back", on_click=lambda e: page.go("/main")),
                                        ElevatedButton(text="Press", on_click=lambda e: _add_text(e=e)),
                                    ],
                                    alignment=MainAxisAlignment.CENTER,
                                ),
                            ],
                            alignment=MainAxisAlignment.CENTER,
                        ),
                    ],
                ),
            )
        if page.route == "/profile":
            page.views.append(
                View(
                    route="/profile",
                    appbar=AppBar(title=Text("Profile"), bgcolor=colors.SURFACE_VARIANT),
                    navigation_bar=nav,
                    controls=[
                        Row(
                            controls=[
                                Text("Profile"),
                                Column(
                                    controls=[
                                        ElevatedButton(text="Back", on_click=lambda e: page.go("/")),
                                        ElevatedButton(text="Press", on_click=lambda e: _add_text(e=e)),
                                    ],
                                    alignment=MainAxisAlignment.CENTER,
                                ),
                            ],
                            alignment=MainAxisAlignment.CENTER,
                        ),
                    ],
                ),
            )
        if page.route == "/settings" or page.route == "/settings/web":
            page.views.append(
                View(
                    route="/settings",
                    appbar=AppBar(title=Text("Settings"), bgcolor=colors.SURFACE_VARIANT),
                    navigation_bar=nav,
                    controls=[
                        Row(
                            controls=[
                                Text("Settings"),
                                Column(
                                    controls=[
                                        ElevatedButton(text="Next", on_click=lambda e: page.go("/settings/web")),
                                        ElevatedButton(text="Back", on_click=lambda e: page.go("/")),
                                        ElevatedButton(text="Press", on_click=lambda e: _add_text(e=e)),
                                    ],
                                    alignment=MainAxisAlignment.CENTER,
                                ),
                            ],
                            alignment=MainAxisAlignment.CENTER,
                        ),
                    ],
                ),
            )
        if page.route == "/settings/web":
            page.views.append(
                View(
                    route="/settings/web",
                    appbar=AppBar(title=Text("Settings Web"), bgcolor=colors.SURFACE_VARIANT),
                    navigation_bar=nav,
                    controls=[
                        Row(
                            controls=[
                                Text("Settings Web"),
                                Column(
                                    controls=[
                                        ElevatedButton(text="Back", on_click=lambda e: page.go("/settings")),
                                        ElevatedButton(text="Press", on_click=lambda e: _add_text(e=e)),
                                    ],
                                    alignment=MainAxisAlignment.CENTER,
                                ),
                            ],
                            alignment=MainAxisAlignment.CENTER,
                        ),
                    ],
                ),
            )
        page.update()

    def view_pop(view: ViewPopEvent) -> None:
        page.views.pop()
        top_view = page.views[-1]
        page.go(str(top_view.route))

    def _on_press(e: ControlEvent) -> None:
        match e.control.selected_index:
            case 0:
                page.go("/")
            case 1:
                page.go("/profile")
            case 2:
                page.go("/settings")

    nav: NavigationBar = NavigationBar(
        on_change=_on_press,
        destinations=[
            NavigationBarDestination(
                icon=icons.HOME,
                selected_icon=icons.HOME,
                label="Main"
            ),
            NavigationBarDestination(
                icon=icons.PERSON,
                selected_icon=icons.PERSON,
                label="Profile"
            ),
            NavigationBarDestination(
                icon=icons.SETTINGS,
                selected_icon=icons.SETTINGS,
                label="Settings",
            ),
        ]
    )

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == "__main__":
    app(target=main)
