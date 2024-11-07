import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TOR @ BOS, 2013-05-12
# https://www.baseball-reference.com/boxes/BOS/BOS201305120.shtml
# https://www.mlb.com/gameday/blue-jays-vs-red-sox/2013/05/12/347305/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-12 13:39-16:52",
        "at": "Fenway Park, Boston, MA",
        "att": "35,532",
        "temp": "68F, Cloudy",
        "wind": "6mph, L To R",
        "away": {
            "team": "Toronto Blue Jays",
            "starter": 64,
            "roster": {
                # Lineup
                53: "Melky Cabrera",
                19: "José Bautista",
                10: "Edwin Encarnación",
                9: "J.P. Arencibia",
                26: "Adam Lind",
                13: "Brett Lawrie",
                28: "Colby Rasmus",
                1: "Emilio Bonifácio",
                66: "Munenori Kawasaki",
                # Starting pitcher
                64: "Chad Jenkins",
                # Bench
                3: "Maicer Izturis",
                16: "Mark DeRosa",
                22: "Henry Blanco",
                # Bullpen
                43: "R.A. Dickey",
                62: "Aaron Loup",
                50: "Steve Delabar",
                56: "Mark Buehrle",
                37: "Mickey Storey",
                38: "Darren Oliver",
                23: "Brandon Morrow",
                49: "Brad Lincoln",
                34: "Ramon Ortiz",
                27: "Brett Cecil",
                44: "Casey Janssen",
                32: "Esmil Rogers",
            },
            "lefties": [62, 56, 38, 27],
            "lineup": [
                [53, "7"],
                [19, "9"],
                [10, "0"],
                [9, "2"],
                [26, "3"],
                [13, "5"],
                [28, "8"],
                [1, "4"],
                [66, "6"],
            ],
            "bench": [
                [3, "3B"],
                [16, "3B"],
                [22, "C"],
            ],
            "bullpen": [43, 62, 50, 56, 37, 38, 23, 49, 34, 27, 44, 32],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 46,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                12: "Mike Napoli",
                29: "Daniel Nava",
                37: "Mike Carp",
                39: "Jarrod Saltalamacchia",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                # Starting pitcher
                46: "Ryan Dempster",
                # Bench
                34: "David Ortiz",
                5: "Jonny Gomes",
                23: "Pedro Ciriaco",
                20: "Ryan Lavarnway",
                # Bullpen
                63: "Alex Wilson",
                65: "Jose De La Torre",
                41: "John Lackey",
                30: "Andrew Miller",
                32: "Craig Breslow",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                22: "Felix Doubront",
            },
            "lefties": [30, 32, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [12, "0"],
                [29, "7"],
                [37, "3"],
                [39, "2"],
                [16, "5"],
                [7, "6"],
            ],
            "bench": [
                [34, "DH"],
                [5, "LF"],
                [23, "3B"],
                [20, "C"],
            ],
            "bullpen": [63, 65, 41, 30, 32, 31, 59, 36, 11, 19, 22],
        },
        "umpires": {
            "HP": "Hunter Wendelstedt",
            "1B": "Jerry Layne",
            "2B": "Alan Porter",
            "3B": "Greg Gibson",
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

# 1. TOR #53 Melky Cabrera (X - X - X)
t1.new_ab()
t1.pitch_list("c f f b s")
t1.out("K")

# 2. TOR #19 José Bautista (X - X - X)
t1.new_ab()
t1.pitch_list("b c")
t1.out("G6-3")

# 3. TOR #10 Edwin Encarnación (X - X - X)
t1.new_ab()
t1.pitch_list("c b f b f")
t1.hit(1)
t1.error(5)
t1.advance(2, "E5")
t1.advance(3, "9 PB")

# 4. TOR #9  J.P. Arencibia (X - 10 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("c b b b s f f")
t1.pb()
t1.out("G4-3")


# Bot 1st
# Pitching: TOR #64 Chad Jenkins
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b f f")
b1.out("P4")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("b c")
b1.out("L8")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("c f f b")
b1.hit(2)

# 4. BOS #12 Mike Napoli (X - 15 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("c")
b1.out("G6-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #46 Ryan Dempster
t2 = game.new_inning()

# 5. TOR #26 Adam Lind (X - X - X)
t2.new_ab()
t2.pitch_list("c f b b f b")
t2.hit(1)
t2.advance(3, "1 2B")
t2.advance(4, "66 1B")

# 6. TOR #13 Brett Lawrie (X - X - 26)
t2.new_ab()
t2.pitch_list("f b f c")
t2.out("!K")

# 7. TOR #28 Colby Rasmus (X - X - 26)
t2.new_ab()
t2.pitch_list("s t f f b c")
t2.out("!K")

# 8. TOR #1  Emilio Bonifácio (X - X - 26)
t2.new_ab()
t2.hit(2)
t2.advance(4, "66 1B")

# 9. TOR #66 Munenori Kawasaki (26 - 1 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("c b l f b b")
t2.hit(1, rbis=2)

# 1. TOR #53 Melky Cabrera (X - X - 66)
t2.new_ab()
t2.out("G4-3")


# Bot 2nd
# Pitching: TOR #64 Chad Jenkins
b2 = game.new_inning()

# 5. BOS #29 Daniel Nava (X - X - X)
b2.new_ab()
b2.pitch_list("c c b f")
b2.out("L7")

# 6. BOS #37 Mike Carp (X - X - X)
b2.new_ab()
b2.pitch_list("c c b b")
b2.out("G6-3")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b2.new_ab()
b2.pitch_list("b c s b")
b2.hit(2)

# 8. BOS #16 Will Middlebrooks (X - 39 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("d")
b2.out("G6-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #46 Ryan Dempster
t3 = game.new_inning()

# 2. TOR #19 José Bautista (X - X - X)
t3.new_ab()
t3.hit(4)

# 3. TOR #10 Edwin Encarnación (X - X - X)
t3.new_ab()
t3.pitch_list("b c b c")
t3.out("G4-3")

# 4. TOR #9  J.P. Arencibia (X - X - X)
t3.new_ab()
t3.pitch_list("f b f f b b")
t3.out("G4-3")

# 5. TOR #26 Adam Lind (X - X - X)
t3.new_ab()
t3.pitch_list("b s")
t3.out("F8")


# Bot 3rd
# Pitching: TOR #64 Chad Jenkins
b3 = game.new_inning()

# 9. BOS #7  Stephen Drew (X - X - X)
b3.new_ab()
b3.pitch_list("c b f b b f")
b3.out("L8")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.pitch_list("b b")
b3.hit(1)
b3.advance(2, "18 1B")

# 2. BOS #18 Shane Victorino (X - X - 2)
b3.new_ab()
b3.pitch_list("b b 1 c c b f")
b3.hit(1)
b3.thrown_out(2, "15 DP6-4-3", 2, 64)

# 3. BOS #15 Dustin Pedroia (X - 2 - 18)
b3.new_ab(is_risp=True)
b3.pitch_list("c f")
b3.out("DP6-4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #46 Ryan Dempster
t4 = game.new_inning()

# 6. TOR #13 Brett Lawrie (X - X - X)
t4.new_ab()
t4.pitch_list("f b b f")
t4.out("G6-3")

# 7. TOR #28 Colby Rasmus (X - X - X)
t4.new_ab()
t4.pitch_list("b b b c b")
t4.reach("BB")
t4.advance(4, "1 HR")

# 8. TOR #1  Emilio Bonifácio (X - X - 28)
t4.new_ab()
t4.pitch_list("b b f")
t4.hit(4, rbis=2)

# 9. TOR #66 Munenori Kawasaki (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("P4")

# 1. TOR #53 Melky Cabrera (X - X - X)
t4.new_ab()
t4.pitch_list("c s b b s")
t4.out("K")


# Bot 4th
# Pitching: TOR #64 Chad Jenkins
b4 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.hit(4)

# 5. BOS #29 Daniel Nava (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("G3")

# 6. BOS #37 Mike Carp (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("F8")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b4.new_ab()
b4.pitch_list("s b f")
b4.out("G3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #46 Ryan Dempster
t5 = game.new_inning()

# 2. TOR #19 José Bautista (X - X - X)
t5.new_ab()
t5.pitch_list("c c")
t5.out("G2-3")

# 3. TOR #10 Edwin Encarnación (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.hit(4)

# 4. TOR #9  J.P. Arencibia (X - X - X)
t5.new_ab()
t5.pitch_list("c c f b s")
t5.out("K")

# 5. TOR #26 Adam Lind (X - X - X)
t5.new_ab()
t5.pitch_list("c b s c")
t5.out("!K")


# Bot 5th
# Pitching: TOR #64 Chad Jenkins
b5 = game.new_inning()

# 8. BOS #16 Will Middlebrooks (X - X - X)
b5.new_ab()
b5.pitch_list("c f b b s")
b5.out("K")

# 9. BOS #7  Stephen Drew (X - X - X)
b5.new_ab()
b5.pitch_list("b b b b")
b5.reach("BB")
b5.advance(2, "2 SB")

# 1. BOS #2  Jacoby Ellsbury (X - X - 7)
b5.new_ab()
b5.pitch_list("c f b b f f d s")
b5.out("K")

# 2. BOS #18 Shane Victorino (X - 7 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b")
b5.out("F7")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #30 Andrew Miller
t6 = game.new_inning()

# Pitching change (BOS): #30 Andrew Miller replaces #46 Ryan Dempster
t6.pitching_substitution(30)

# 6. TOR #13 Brett Lawrie (X - X - X)
t6.new_ab()
t6.pitch_list("b b")
t6.hit(4)

# 7. TOR #28 Colby Rasmus (X - X - X)
t6.new_ab()
t6.pitch_list("b s b b")
t6.out("L8")

# 8. TOR #1  Emilio Bonifácio (X - X - X)
t6.new_ab()
t6.hit(1)
t6.advance(2, "66 BB")
t6.advance(3, "53 SB")
t6.advance(4, "53 SF7")

# 9. TOR #66 Munenori Kawasaki (X - X - 1)
t6.new_ab()
t6.pitch_list("b c b b b")
t6.reach("BB")
t6.advance(2, "53 SB")
t6.advance(4, "19 HR")

# Pitching change (BOS): #59 Clayton Mortensen replaces #30 Andrew Miller
t6.pitching_substitution(59)

# 1. TOR #53 Melky Cabrera (X - 1 - 66)
t6.new_ab(is_risp=True)
t6.pitch_list("b b b c c")
t6.out("SF7", rbis=1)

# 2. TOR #19 José Bautista (X - 66 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("s")
t6.hit(4, rbis=2)

# 3. TOR #10 Edwin Encarnación (X - X - X)
t6.new_ab()
t6.pitch_list("c b b c f c")
t6.out("!K")


# Bot 6th
# Pitching: TOR #64 Chad Jenkins
b6 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b6.new_ab()
b6.pitch_list("c f")
b6.hit(1)
b6.advance(3, "12 2B")
b6.advance(4, "29 SF9")

# 4. BOS #12 Mike Napoli (X - X - 15)
b6.new_ab()
b6.pitch_list("c b t f b f")
b6.hit(2)

# Pitching change (TOR): #62 Aaron Loup replaces #64 Chad Jenkins
b6.pitching_substitution(62)

# 5. BOS #29 Daniel Nava (15 - 12 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("f b")
b6.out("SF9", rbis=1)

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #37 Mike Carp, batting 6th
b6.offensive_substitution(6, 5, "PH")

# 6. BOS #5  Jonny Gomes (X - 12 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("c b s b f s")
b6.out("K")

# 7. BOS #39 Jarrod Saltalamacchia (X - 12 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b b")
b6.out("F9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #59 Clayton Mortensen
t7 = game.new_inning()

# Defensive change (BOS): #23 Pedro Ciriaco replaces #18 Shane Victorino (RF), playing 1B, batting 2nd
t7.defensive_substitution(2, 23, "3")

# Defensive switch (BOS): #29 Daniel Nava moves to RF
t7.defensive_switch(29, "9")

# Defensive switch (BOS): #5 Jonny Gomes moves to LF
t7.defensive_switch(5, "7")

# 4. TOR #9  J.P. Arencibia (X - X - X)
t7.new_ab()
t7.out("F8")

# 5. TOR #26 Adam Lind (X - X - X)
t7.new_ab()
t7.pitch_list("c f")
t7.out("G4-3")

# 6. TOR #13 Brett Lawrie (X - X - X)
t7.new_ab()
t7.out("L8")


# Bot 7th
# Pitching: TOR #62 Aaron Loup
b7 = game.new_inning()

# 8. BOS #16 Will Middlebrooks (X - X - X)
b7.new_ab()
b7.pitch_list("c b f b s")
b7.out("K")

# 9. BOS #7  Stephen Drew (X - X - X)
b7.new_ab()
b7.pitch_list("c f f s")
b7.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b7.new_ab()
b7.pitch_list("b f")
b7.out("G3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #32 Craig Breslow
t8 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #59 Clayton Mortensen
t8.pitching_substitution(32)

# 7. TOR #28 Colby Rasmus (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("G3-1")

# 8. TOR #1  Emilio Bonifácio (X - X - X)
t8.new_ab()
t8.out("P4")

# 9. TOR #66 Munenori Kawasaki (X - X - X)
t8.new_ab()
t8.pitch_list("f f b f b b c")
t8.out("!K")


# Bot 8th
# Pitching: TOR #32 Esmil Rogers
b8 = game.new_inning()

# Pitching change (TOR): #32 Esmil Rogers replaces #62 Aaron Loup
b8.pitching_substitution(32)

# 2. BOS #23 Pedro Ciriaco (X - X - X)
b8.new_ab()
b8.hit(4)

# 3. BOS #15 Dustin Pedroia (X - X - X)
b8.new_ab()
b8.pitch_list("b c")
b8.out("F9")

# 4. BOS #12 Mike Napoli (X - X - X)
b8.new_ab()
b8.pitch_list("c b")
b8.hit(1)
b8.advance(2, "29 BB")
b8.advance(3, "5 HBP")
b8.advance(4, "39 FC6-4")

# 5. BOS #29 Daniel Nava (X - X - 12)
b8.new_ab()
b8.pitch_list("b c b b s b")
b8.reach("BB")
b8.advance(2, "5 HBP")
b8.advance(3, "39 FC6-4")

# 6. BOS #5  Jonny Gomes (X - 12 - 29)
b8.new_ab(is_risp=True)
b8.pitch_list("c d f")
b8.reach("HBP")
b8.thrown_out(2, "39 FC6-4", 2, 27)

# Pitching change (TOR): #27 Brett Cecil replaces #32 Esmil Rogers
b8.pitching_substitution(27)

# 7. BOS #39 Jarrod Saltalamacchia (12 - 29 - 5)
b8.new_ab(is_risp=True)
b8.pitch_list("c")
b8.reach("FC6-4", rbis=1)
b8.thrown_out(2, "16 FC5-4", 3, 27)

# 8. BOS #16 Will Middlebrooks (29 - X - 39)
b8.new_ab(is_risp=True)
b8.pitch_list("f b b f")
b8.reach("FC5-4")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #65 Jose De La Torre
t9 = game.new_inning()

# Pitching change (BOS): #65 Jose De La Torre replaces #32 Craig Breslow
t9.pitching_substitution(65)

# 1. TOR #53 Melky Cabrera (X - X - X)
t9.new_ab()
t9.pitch_list("b b f b c")
t9.hit(2)
t9.advance(4, "10 1B")

# 2. TOR #19 José Bautista (X - 53 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("b b b b")
t9.reach("BB")
t9.advance(3, "10 1B")
t9.advance(4, "9 DP6-4-3")

# 3. TOR #10 Edwin Encarnación (X - 53 - 19)
t9.new_ab(is_risp=True)
t9.pitch_list("c")
t9.hit(1, rbis=1)
t9.thrown_out(2, "9 DP6-4-3", 1, 65)

# 4. TOR #9  J.P. Arencibia (19 - X - 10)
t9.new_ab(is_risp=True)
t9.pitch_list("b c")
t9.out("DP6-4-3")

# 5. TOR #26 Adam Lind (X - X - X)
t9.new_ab()
t9.pitch_list("b c b")
t9.out("G3")


# Bot 9th
# Pitching: TOR #50 Steve Delabar
b9 = game.new_inning()

# Pitching change (TOR): #50 Steve Delabar replaces #27 Brett Cecil
b9.pitching_substitution(50)

# 9. BOS #7  Stephen Drew (X - X - X)
b9.new_ab()
b9.pitch_list("c b b")
b9.hit(1)

# 1. BOS #2  Jacoby Ellsbury (X - X - 7)
b9.new_ab()
b9.pitch_list("d b c f c")
b9.out("!K")

# 2. BOS #23 Pedro Ciriaco (X - X - 7)
b9.new_ab()
b9.pitch_list("c b d b s")
b9.out("F8")

# 3. BOS #15 Dustin Pedroia (X - X - 7)
b9.new_ab()
b9.pitch_list("c b")
b9.out("F8")

# Winning team: TOR
# WP: TOR #64 Chad Jenkins
game.winning_pitcher(64, is_away_team=True)

# Loser team: BOS
# LP: BOS #46 Ryan Dempster
game.losing_pitcher(46)

# print(game)
game.generate_scorecard()
