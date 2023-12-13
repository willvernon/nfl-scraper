import scrapy


class NFLScores(scrapy.Spider):
    name = "nfl_scores"
    start_urls = ["https://www.pro-football-reference.com/"]
    custom_settings = {
        'FEED_EXPORT_FIELDS': ["date", "winning_team", "winning_team_score", "losing_team", "losing_team_score"],
    }
    def parse(self, response):
        game = 1
        while game <= 15:
            date = response.xpath(
                f'//*[@id="scores"]/div[2]/div[{game}]/table[1]/tbody/tr[1]/td/text()'
            ).extract_first()
            winning_team = response.xpath(
                f'//*[@id="scores"]/div[2]/div[{game}]/table[1]/tbody/tr[2]/td[1]/a/text()'
            ).extract_first()
            winning_team_score = response.xpath(
                f'//*[@id="scores"]/div[2]/div[{game}]/table[1]/tbody/tr[2]/td[2]/text()'
            ).extract_first()
            losing_team = response.xpath(
                f'//*[@id="scores"]/div[2]/div[{game}]/table[1]/tbody/tr[3]/td[1]/a/text()'
            ).extract_first()
            losing_team_score = response.xpath(
                f'//*[@id="scores"]/div[2]/div[{game}]/table[1]/tbody/tr[3]/td[2]/text()'
            ).extract_first()
            yield {
                "date": date,
                "winning_team": winning_team,
                "winning_team_score": winning_team_score,
                "losing_team": losing_team,
                "losing_team_score": losing_team_score,
            }
            game += 1

    # def parse(self, response):
    #     # Extract data from the response
    #     # This is just an example and will need to be modified to suit the specific structure of the webpage you're scraping
    #     for games in response.css("game_summaries"):
    #         yield {
    #             "data": games.xpath("//*[@id='scores']/div[2]/div[1]/table[1]/tbody/tr[2]/td[1]/a/text()").get(),
    #             "date": games.xpath("/div[1]/table[1]/tbody/tr[1]/td/text()").get(),
    #             "time": games.css("div.game_summary::text").get(),
    #             "away_team": games.css("div.game_summary::text").get(),
    #             "away_score": games.css("div.game_summary::text").get(),
    #             "home_team": games.css("div.game_summary::text").get(),
    #             "home_score": games.css("div.game_summary::text").get(),
    #         }

    #     for item in response.css("div.item"):
    #         yield {
    #             "title": item.css("h2.title::text").get(),
    #             "description": item.css("p.description::text").get(),
    #         }

    #     # Follow links to next pages
    #     # This is just an example and will need to be modified to suit the specific structure of the webpage you're scraping
    #     for href in response.css("a.next-page::attr(href)"):
    #         yield response.follow(href, self.parse)
