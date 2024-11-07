import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TOR @ BOS, 2013-06-30
# https://www.baseball-reference.com/boxes/BOS/BOS201306300.shtml
# https://www.mlb.com/gameday/blue-jays-vs-red-sox/2013/06/30/347970/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-06-30 13:37-16:47",
        "at": "Fenway Park, Boston, MA",
        "att": "37,425",
        "temp": "83F, Cloudy",
        "wind": "12mph, Out To CF",
        "away": {
            "team": "Toronto Blue Jays",
            "starter": 56,
            "roster": {
                # Lineup
                7: "José Reyes",
                19: "José Bautista",
                10: "Edwin Encarnación",
                26: "Adam Lind",
                11: "Rajai Davis",
                28: "Colby Rasmus",
                9: "J.P. Arencibia",
                3: "Maicer Izturis",
                66: "Munenori Kawasaki",
                # Starting pitcher
                56: "Mark Buehrle",
                # Bench
                1: "Emilio Bonifácio",
                16: "Mark DeRosa",
                22: "Josh Thole",
                # Bullpen
                43: "R.A. Dickey",
                45: "Neil Wagner",
                62: "Aaron Loup",
                57: "Juan Pablo Perez",
                50: "Steve Delabar",
                67: "Chien-Ming Wang",
                55: "Josh Johnson",
                38: "Darren Oliver",
                29: "Dustin McGowan",
                27: "Brett Cecil",
                44: "Casey Janssen",
                32: "Esmil Rogers",
            },
            "lefties": [56, 62, 57, 38, 27],
            "lineup": [
                [7, "6"],
                [19, "9"],
                [10, "0"],
                [26, "3"],
                [11, "7"],
                [28, "8"],
                [9, "2"],
                [3, "5"],
                [66, "4"],
            ],
            "bench": [
                [1, "2B"],
                [16, "3B"],
                [22, "C"],
            ],
            "bullpen": [43, 45, 62, 57, 50, 67, 55, 38, 29, 27, 44, 32],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 46,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                5: "Jonny Gomes",
                12: "Mike Napoli",
                29: "Daniel Nava",
                20: "Ryan Lavarnway",
                10: "Jose Iglesias",
                23: "Brandon Snyder",
                # Starting pitcher
                46: "Ryan Dempster",
                # Bench
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                76: "Jonathan Diaz",
                34: "David Ortiz",
                # Bullpen
                64: "Allen Webster",
                63: "Alex Wilson",
                40: "Andrew Bailey",
                41: "John Lackey",
                30: "Andrew Miller",
                32: "Craig Breslow",
                19: "Koji Uehara",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                22: "Felix Doubront",
            },
            "lefties": [30, 32, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [5, "7"],
                [12, "0"],
                [29, "3"],
                [20, "2"],
                [10, "6"],
                [23, "5"],
            ],
            "bench": [
                [39, "C"],
                [37, "1B"],
                [76, "SS"],
                [34, "DH"],
            ],
            "bullpen": [64, 63, 40, 41, 30, 32, 19, 31, 36, 22],
        },
        "umpires": {
            "HP": "Tim Welke",
            "1B": "Mike Everitt",
            "2B": "Bruce Dreckman",
            "3B": "Dan Bellino",
        },
    },
)

##########################################################
# PLAY BALL!
##########################################################


##########################################################
# 1st Inning
##########################################################
# Top 1st
# Pitching: BOS #46 Ryan Dempster
t1 = game.new_inning()

# 1. TOR #7  José Reyes (X - X - X)
t1.new_ab()
t1.pitch_list("c c b s")
t1.out("K")

# 2. TOR #19 José Bautista (X - X - X)
t1.new_ab()
t1.pitch_list("b b f c b f")
t1.out("F9")

# 3. TOR #10 Edwin Encarnación (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.out("G5-3")


# Bot 1st
# Pitching: TOR #56 Mark Buehrle
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("c f b")
b1.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("F8")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("c b b b b")
b1.reach("BB")

# 4. BOS #5  Jonny Gomes (X - X - 15)
b1.new_ab()
b1.pitch_list("s")
b1.out("G1-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #46 Ryan Dempster
t2 = game.new_inning()

# 4. TOR #26 Adam Lind (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("G4-3")

# 5. TOR #11 Rajai Davis (X - X - X)
t2.new_ab()
t2.pitch_list("c c s")
t2.out("K")

# 6. TOR #28 Colby Rasmus (X - X - X)
t2.new_ab()
t2.pitch_list("b b c f f f b")
t2.out("L8")


# Bot 2nd
# Pitching: TOR #56 Mark Buehrle
b2 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
b2.new_ab()
b2.pitch_list("b c f")
b2.hit(1)
b2.advance(2, "29 1B")
b2.advance(4, "20 2B")

# 6. BOS #29 Daniel Nava (X - X - 12)
b2.new_ab()
b2.pitch_list("c b 1")
b2.hit(1)
b2.advance(3, "20 2B")
b2.advance(4, "23 2B")

# 7. BOS #20 Ryan Lavarnway (X - 12 - 29)
b2.new_ab(is_risp=True)
b2.pitch_list("c")
b2.hit(2, rbis=1)
b2.advance(4, "23 2B")

# 8. BOS #10 Jose Iglesias (29 - 20 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("c b s f f s")
b2.out("K")

# 9. BOS #23 Brandon Snyder (29 - 20 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("c f")
b2.hit(2, rbis=2)
b2.thrown_out(3, "15 FC5", 3, 56)

# 1. BOS #2  Jacoby Ellsbury (X - 23 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b f b f")
b2.reach("HBP")
b2.advance(2, "15 FC5")

# 2. BOS #18 Shane Victorino (X - 23 - 2)
b2.new_ab(is_risp=True)
b2.pitch_list("b b b c c f c")
b2.out("!K")

# 3. BOS #15 Dustin Pedroia (X - 23 - 2)
b2.new_ab(is_risp=True)
b2.pitch_list("b")
b2.reach("FC5")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #46 Ryan Dempster
t3 = game.new_inning()

# 7. TOR #9  J.P. Arencibia (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("(F)P3")

# 8. TOR #3  Maicer Izturis (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("L7")

# 9. TOR #66 Munenori Kawasaki (X - X - X)
t3.new_ab()
t3.pitch_list("c b l f f")
t3.hit(1)
t3.advance(2, "7 BB")

# 1. TOR #7  José Reyes (X - X - 66)
t3.new_ab()
t3.pitch_list("b b b b")
t3.reach("BB")

# 2. TOR #19 José Bautista (X - 66 - 7)
t3.new_ab(is_risp=True)
t3.pitch_list("c c b")
t3.out("G1-3")


# Bot 3rd
# Pitching: TOR #56 Mark Buehrle
b3 = game.new_inning()

# Defensive change (TOR): #22 Josh Thole replaces #26 Adam Lind (1B), playing 1B, batting 4th
b3.defensive_substitution(4, 22, "3")

# 4. BOS #5  Jonny Gomes (X - X - X)
b3.new_ab()
b3.pitch_list("b b c f f s")
b3.out("K")

# 5. BOS #12 Mike Napoli (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.out("F8")

# 6. BOS #29 Daniel Nava (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("G4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #46 Ryan Dempster
t4 = game.new_inning()

# 3. TOR #10 Edwin Encarnación (X - X - X)
t4.new_ab()
t4.pitch_list("c b b f b")
t4.hit(1)
t4.advance(2, "11 1B")
t4.advance(4, "28 1B")

# 4. TOR #22 Josh Thole (X - X - 10)
t4.new_ab()
t4.pitch_list("c s f")
t4.out("F7")

# 5. TOR #11 Rajai Davis (X - X - 10)
t4.new_ab()
t4.pitch_list("1 b s")
t4.hit(1)
t4.advance(2, "28 1B")
t4.advance(3, "9 SB")
t4.advance(4, "3 FC3-6")

# 6. TOR #28 Colby Rasmus (X - 10 - 11)
t4.new_ab(is_risp=True)
t4.pitch_list("c b b")
t4.hit(1, rbis=1)
t4.advance(2, "9 BB")
t4.advance(3, "3 FC3-6")

# 7. TOR #9  J.P. Arencibia (X - 11 - 28)
t4.new_ab(is_risp=True)
t4.pitch_list("c 2 b d b b")
t4.reach("BB")
t4.thrown_out(2, "3 FC3-6", 2, 46)

# 8. TOR #3  Maicer Izturis (11 - 28 - 9)
t4.new_ab(is_risp=True)
t4.pitch_list("c b f b")
t4.reach("FC3-6", rbis=1)
t4.thrown_out(2, "66 FC4-6", 3, 46)

# 9. TOR #66 Munenori Kawasaki (28 - X - 3)
t4.new_ab(is_risp=True)
t4.pitch_list("c")
t4.reach("FC4-6")


# Bot 4th
# Pitching: TOR #56 Mark Buehrle
b4 = game.new_inning()

# 7. BOS #20 Ryan Lavarnway (X - X - X)
b4.new_ab()
b4.pitch_list("b b b c f")
b4.out("L8")

# 8. BOS #10 Jose Iglesias (X - X - X)
b4.new_ab()
b4.out("G4-3")

# 9. BOS #23 Brandon Snyder (X - X - X)
b4.new_ab()
b4.pitch_list("c b b b")
b4.out("F9")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #46 Ryan Dempster
t5 = game.new_inning()

# 1. TOR #7  José Reyes (X - X - X)
t5.new_ab()
t5.pitch_list("b b")
t5.out("G3-1")

# 2. TOR #19 José Bautista (X - X - X)
t5.new_ab()
t5.hit(1)
t5.thrown_out(2, "10 DP6-4-3", 2, 46)

# 3. TOR #10 Edwin Encarnación (X - X - 19)
t5.new_ab()
t5.pitch_list("c s f")
t5.out("DP6-4-3")


# Bot 5th
# Pitching: TOR #56 Mark Buehrle
b5 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.hit(1)
b5.advance(2, "18 G5-3")
b5.advance(4, "5 2B")

# 2. BOS #18 Shane Victorino (X - X - 2)
b5.new_ab()
b5.pitch_list("l f f d 1 f 1")
b5.out("G5-3")

# 3. BOS #15 Dustin Pedroia (X - 2 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b b c f f f s")
b5.out("K")

# 4. BOS #5  Jonny Gomes (X - 2 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("f b f")
b5.hit(2, rbis=1)

# 5. BOS #12 Mike Napoli (X - 5 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("c")
b5.out("F7")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #46 Ryan Dempster
t6 = game.new_inning()

# 4. TOR #22 Josh Thole (X - X - X)
t6.new_ab()
t6.pitch_list("b b b b")
t6.reach("BB")
t6.advance(2, "11 1B")
t6.advance(3, "28 1B")

# 5. TOR #11 Rajai Davis (X - X - 22)
t6.new_ab()
t6.hit(1)
t6.advance(2, "28 1B")

# 6. TOR #28 Colby Rasmus (X - 22 - 11)
t6.new_ab(is_risp=True)
t6.pitch_list("b")
t6.hit(1)

# 7. TOR #9  J.P. Arencibia (22 - 11 - 28)
t6.new_ab(is_risp=True)
t6.pitch_list("s d d t f f")
t6.out("IF6")

# Pitching change (BOS): #32 Craig Breslow replaces #46 Ryan Dempster
t6.pitching_substitution(32)

# 8. TOR #3  Maicer Izturis (22 - 11 - 28)
t6.new_ab(is_risp=True)
t6.pitch_list("f f")
t6.out("IF6")

# Offensive change (TOR): Pinch-hitter #1 Emilio Bonifácio replaces #66 Munenori Kawasaki, batting 9th
t6.offensive_substitution(9, 1, "PH")

# 9. TOR #1  Emilio Bonifácio (22 - 11 - 28)
t6.new_ab(is_risp=True)
t6.pitch_list("b b s f s")
t6.out("K")


# Bot 6th
# Pitching: TOR #56 Mark Buehrle
b6 = game.new_inning()

# Defensive switch (TOR): #1 Emilio Bonifácio moves to 2B
b6.defensive_switch(1, "4")

# 6. BOS #29 Daniel Nava (X - X - X)
b6.new_ab()
b6.pitch_list("c b b f")
b6.out("G5-3")

# 7. BOS #20 Ryan Lavarnway (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("F8")

# 8. BOS #10 Jose Iglesias (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.hit(1)

# 9. BOS #23 Brandon Snyder (X - X - 10)
b6.new_ab()
b6.pitch_list("b b f 1 1 f f")
b6.out("F7")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #32 Craig Breslow
t7 = game.new_inning()

# 1. TOR #7  José Reyes (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.hit(4)

# Pitching change (BOS): #63 Alex Wilson replaces #32 Craig Breslow
t7.pitching_substitution(63)

# 2. TOR #19 José Bautista (X - X - X)
t7.new_ab()
t7.hit(1)

# 3. TOR #10 Edwin Encarnación (X - X - 19)
t7.new_ab()
t7.pitch_list("b b")
t7.out("P4")

# Pitching change (BOS): #30 Andrew Miller replaces #63 Alex Wilson
t7.pitching_substitution(30)

# 4. TOR #22 Josh Thole (X - X - 19)
t7.new_ab()
t7.pitch_list("f f b d b s")
t7.out("K")

# 5. TOR #11 Rajai Davis (X - X - 19)
t7.new_ab()
t7.pitch_list("s s c")
t7.out("!K")


# Bot 7th
# Pitching: TOR #29 Dustin McGowan
b7 = game.new_inning()

# Pitching change (TOR): #29 Dustin McGowan replaces #56 Mark Buehrle
b7.pitching_substitution(29)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b7.new_ab()
b7.pitch_list("b s c f b f f f s")
b7.out("K")

# 2. BOS #18 Shane Victorino (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("G1-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b7.new_ab()
b7.pitch_list("b b")
b7.out("G6-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #30 Andrew Miller
t8 = game.new_inning()

# 6. TOR #28 Colby Rasmus (X - X - X)
t8.new_ab()
t8.out("B1-3")

# 7. TOR #9  J.P. Arencibia (X - X - X)
t8.new_ab()
t8.pitch_list("b f")
t8.out("G5-3")

# 8. TOR #3  Maicer Izturis (X - X - X)
t8.new_ab()
t8.pitch_list("b f b b f b")
t8.reach("BB")

# 9. TOR #1  Emilio Bonifácio (X - X - 3)
t8.new_ab()
t8.out("F8")


# Bot 8th
# Pitching: TOR #29 Dustin McGowan
b8 = game.new_inning()

# 4. BOS #5  Jonny Gomes (X - X - X)
b8.new_ab()
b8.pitch_list("c b b c f f")
b8.out("P5")

# 5. BOS #12 Mike Napoli (X - X - X)
b8.new_ab()
b8.pitch_list("c f b b b s")
b8.out("K")

# 6. BOS #29 Daniel Nava (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.hit(1)
b8.thrown_out(2, "20 FC4-6", 3, 29)

# 7. BOS #20 Ryan Lavarnway (X - X - 29)
b8.new_ab()
b8.pitch_list("c b")
b8.reach("FC4-6")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #19 Koji Uehara
t9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #30 Andrew Miller
t9.pitching_substitution(19)

# 1. TOR #7  José Reyes (X - X - X)
t9.new_ab()
t9.pitch_list("c f b b")
t9.out("F9")

# 2. TOR #19 José Bautista (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.hit(4)

# 3. TOR #10 Edwin Encarnación (X - X - X)
t9.new_ab()
t9.pitch_list("f")
t9.hit(1)

# 4. TOR #22 Josh Thole (X - X - 10)
t9.new_ab()
t9.pitch_list("c b f b b f f t")
t9.out("KT")

# 5. TOR #11 Rajai Davis (X - X - 10)
t9.new_ab()
t9.pitch_list("1 c")
t9.out("L4")


# Bot 9th
# Pitching: TOR #57 Juan Pablo Perez
b9 = game.new_inning()

# Pitching change (TOR): #57 Juan Pablo Perez replaces #29 Dustin McGowan
b9.pitching_substitution(57)

# 8. BOS #10 Jose Iglesias (X - X - X)
b9.new_ab()
b9.out("G4-3")

# 9. BOS #23 Brandon Snyder (X - X - X)
b9.new_ab()
b9.pitch_list("b c")
b9.hit(1)
b9.advance(2, "2 BB")
# Offensive change (BOS): Pinch-runner #76 Jonathan Diaz replaces #23 Brandon Snyder
b9.offensive_substitution(9, 76, "PR")
b9.atbase("PR")
b9.advance("U", "18 E3")

# 1. BOS #2  Jacoby Ellsbury (X - X - 23)
b9.new_ab()
b9.pitch_list("b s 1 b b b")
b9.reach("BB")
b9.advance(2, "18 E3")

# Pitching change (TOR): #44 Casey Janssen replaces #57 Juan Pablo Perez
b9.pitching_substitution(44)

# 2. BOS #18 Shane Victorino (X - 23 - 2)
b9.new_ab(is_risp=True)
b9.pitch_list("c")
b9.error(3)
b9.reach("E3")

# Winning team: BOS
# WP: BOS #19 Koji Uehara
game.winning_pitcher(19)

# Loser team: TOR
# LP: TOR #57 Juan Pablo Perez
game.losing_pitcher(57, is_away_team=True)

# print(game)
game.generate_scorecard()
