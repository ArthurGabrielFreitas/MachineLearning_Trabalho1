class Contato:
    def __init__(self, nome, telefone, user_twitter, user_facebook, user_instagram):
        self.nome = nome
        self.telefone = telefone
        self.user_twitter = user_twitter
        self.user_facebook = user_facebook
        self.user_instagram = user_instagram

    def __str__(self):
        return f'Nome: {self.nome}\t\tTelefone: {self.telefone}\t\tTwitter: {self.user_twitter}' \
               f'\t\tFacebook: {self.user_facebook}\t\tInstagram: {self.user_instagram} '

    def escrever_csv(self):
        return f'\n{self.nome},{self.telefone},{self.user_twitter},{self.user_facebook},{self.user_instagram}'
