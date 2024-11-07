import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TOR @ BOS, 2013-05-11
# https://www.baseball-reference.com/boxes/BOS/BOS201305110.shtml
# https://www.mlb.com/gameday/blue-jays-vs-red-sox/2013/05/11/347292/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-11 14:26-17:58 (0:50 delay)",
        "at": "Fenway Park, Boston, MA",
        "att": "36,543",
        "temp": "63F, Drizzle",
        "wind": "19mph, Out To RF",
        "away": {
            "team": "Toronto Blue Jays",
            "starter": 56,
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
                56: "Mark Buehrle",
                # Bench
                3: "Maicer Izturis",
                16: "Mark DeRosa",
                22: "Henry Blanco",
                # Bullpen
                43: "R.A. Dickey",
                62: "Aaron Loup",
                50: "Steve Delabar",
                64: "Chad Jenkins",
                37: "Mickey Storey",
                38: "Darren Oliver",
                23: "Brandon Morrow",
                49: "Brad Lincoln",
                34: "Ramon Ortiz",
                27: "Brett Cecil",
                44: "Casey Janssen",
                32: "Esmil Rogers",
            },
            "lefties": [56, 62, 38, 27],
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
            "bullpen": [43, 62, 50, 64, 37, 38, 23, 49, 34, 27, 44, 32],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 11,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                5: "Jonny Gomes",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                3: "David Ross",
                # Starting pitcher
                11: "Clay Buchholz",
                # Bench
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                29: "Daniel Nava",
                23: "Pedro Ciriaco",
                # Bullpen
                63: "Alex Wilson",
                65: "Jose De La Torre",
                41: "John Lackey",
                30: "Andrew Miller",
                32: "Craig Breslow",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [30, 32, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [5, "7"],
                [16, "5"],
                [7, "6"],
                [3, "2"],
            ],
            "bench": [
                [39, "C"],
                [37, "1B"],
                [29, "LF"],
                [23, "3B"],
            ],
            "bullpen": [63, 65, 41, 30, 32, 31, 59, 36, 19, 22, 46],
        },
        "umpires": {
            "HP": "Greg Gibson",
            "1B": "Hunter Wendelstedt",
            "2B": "Jerry Layne",
            "3B": "Alan Porter",
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
# Pitching: BOS #11 Clay Buchholz
t1 = game.new_inning()

# 1. TOR #53 Melky Cabrera (X - X - X)
t1.new_ab()
t1.pitch_list("c c s")
t1.out("K")

# 2. TOR #19 José Bautista (X - X - X)
t1.new_ab()
t1.pitch_list("b s f c")
t1.out("!K")

# 3. TOR #10 Edwin Encarnación (X - X - X)
t1.new_ab()
t1.out("F9")


# Bot 1st
# Pitching: TOR #56 Mark Buehrle
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.hit(1)
b1.advance(2, "15 1B")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b1.new_ab()
b1.pitch_list("c b 1 1")
b1.hit(1)

# 4. BOS #34 David Ortiz (X - 18 - 15)
b1.new_ab(is_risp=True)
b1.pitch_list("c f f b")
b1.out("F9")

# 5. BOS #12 Mike Napoli (X - 18 - 15)
b1.new_ab(is_risp=True)
b1.pitch_list("b c")
b1.out("F8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #11 Clay Buchholz
t2 = game.new_inning()

# 4. TOR #9  J.P. Arencibia (X - X - X)
t2.new_ab()
t2.pitch_list("b f s b")
t2.out("G3")

# 5. TOR #26 Adam Lind (X - X - X)
t2.new_ab()
t2.pitch_list("c f")
t2.hit(1)
t2.thrown_out(2, "13 DP4-6-3", 2, 11)

# 6. TOR #13 Brett Lawrie (X - X - 26)
t2.new_ab()
t2.pitch_list("c 1")
t2.out("DP4-6-3")


# Bot 2nd
# Pitching: TOR #56 Mark Buehrle
b2 = game.new_inning()

# 6. BOS #5  Jonny Gomes (X - X - X)
b2.new_ab()
b2.pitch_list("b c")
b2.out("F8")

# 7. BOS #16 Will Middlebrooks (X - X - X)
b2.new_ab()
b2.pitch_list("c b")
b2.hit(2)

# 8. BOS #7  Stephen Drew (X - 16 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b b c b b")
b2.reach("BB")

# 9. BOS #3  David Ross (X - 16 - 7)
b2.new_ab(is_risp=True)
b2.pitch_list("b f b f t")
b2.out("KT")

# 1. BOS #2  Jacoby Ellsbury (X - 16 - 7)
b2.new_ab(is_risp=True)
b2.pitch_list("f f b b")
b2.out("G3-1")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #11 Clay Buchholz
t3 = game.new_inning()

# 7. TOR #28 Colby Rasmus (X - X - X)
t3.new_ab()
t3.pitch_list("b b b b")
t3.reach("BB")
t3.advance(2, "66 B2-3")
t3.advance(4, "53 1B")

# 8. TOR #1  Emilio Bonifácio (X - X - 28)
t3.new_ab()
t3.pitch_list("c 1 1 f b b 1 c")
t3.out("!K")

# 9. TOR #66 Munenori Kawasaki (X - X - 28)
t3.new_ab()
t3.out("B2-3")

# 1. TOR #53 Melky Cabrera (X - 28 - X)
t3.new_ab(is_risp=True)
t3.hit(1, rbis=1)
t3.advance(2, "19 1B")
t3.advance(3, "10 BB")

# 2. TOR #19 José Bautista (X - X - 53)
t3.new_ab()
t3.pitch_list("s b 1 f b")
t3.hit(1)
t3.advance(2, "10 BB")

# 3. TOR #10 Edwin Encarnación (X - 53 - 19)
t3.new_ab(is_risp=True)
t3.pitch_list("b s b f f b b")
t3.reach("BB")

# 4. TOR #9  J.P. Arencibia (53 - 19 - 10)
t3.new_ab(is_risp=True)
t3.pitch_list("c b")
t3.out("P4")


# Bot 3rd
# Pitching: TOR #56 Mark Buehrle
b3 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b3.new_ab()
b3.pitch_list("c s t")
b3.out("KT")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b3.new_ab()
b3.pitch_list("c f")
b3.hit(1)
b3.thrown_out(2, "7-4", 2, 56)

# 4. BOS #34 David Ortiz (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.hit(1)

# 5. BOS #12 Mike Napoli (X - X - 34)
b3.new_ab()
b3.pitch_list("f c c")
b3.out("!K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #11 Clay Buchholz
t4 = game.new_inning()

# 5. TOR #26 Adam Lind (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.hit(1)
t4.advance(2, "13 G5-3")
t4.advance(4, "28 1B")

# 6. TOR #13 Brett Lawrie (X - X - 26)
t4.new_ab()
t4.pitch_list("c")
t4.out("G5-3")

# 7. TOR #28 Colby Rasmus (X - 26 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b c f")
t4.hit(1, rbis=1)
t4.thrown_out(2, "1 DP4-6-3", 2, 11)

# 8. TOR #1  Emilio Bonifácio (X - X - 28)
t4.new_ab()
t4.pitch_list("1 1")
t4.out("DP4-6-3")


# Bot 4th
# Pitching: TOR #56 Mark Buehrle
b4 = game.new_inning()

# 6. BOS #5  Jonny Gomes (X - X - X)
b4.new_ab()
b4.pitch_list("c b s b b f")
b4.out("(F)P2")

# 7. BOS #16 Will Middlebrooks (X - X - X)
b4.new_ab()
b4.pitch_list("c b s b s")
b4.out("K")

# 8. BOS #7  Stephen Drew (X - X - X)
b4.new_ab()
b4.pitch_list("f c b b f b")
b4.out("G6-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #11 Clay Buchholz
t5 = game.new_inning()

# 9. TOR #66 Munenori Kawasaki (X - X - X)
t5.new_ab()
t5.pitch_list("b c f")
t5.out("G1-3")

# 1. TOR #53 Melky Cabrera (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("G6-3")

# 2. TOR #19 José Bautista (X - X - X)
t5.new_ab()
t5.pitch_list("b b c s b b")
t5.reach("BB")

# 3. TOR #10 Edwin Encarnación (X - X - 19)
t5.new_ab()
t5.out("G5-3")


# Bot 5th
# Pitching: TOR #56 Mark Buehrle
b5 = game.new_inning()

# 9. BOS #3  David Ross (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("G6-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b5.new_ab()
b5.pitch_list("f f f")
b5.out("P6")

# 2. BOS #18 Shane Victorino (X - X - X)
b5.new_ab()
b5.out("F8")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #11 Clay Buchholz
t6 = game.new_inning()

# 4. TOR #9  J.P. Arencibia (X - X - X)
t6.new_ab()
t6.pitch_list("c s")
t6.out("G5-3")

# 5. TOR #26 Adam Lind (X - X - X)
t6.new_ab()
t6.pitch_list("c b b b")
t6.out("G3-1")

# 6. TOR #13 Brett Lawrie (X - X - X)
t6.new_ab()
t6.out("L9")


# Bot 6th
# Pitching: TOR #56 Mark Buehrle
b6 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b6.new_ab()
b6.pitch_list("c b")
b6.out("G1-3")

# 4. BOS #34 David Ortiz (X - X - X)
b6.new_ab()
b6.pitch_list("b f f")
b6.out("F8")

# 5. BOS #12 Mike Napoli (X - X - X)
b6.new_ab()
b6.pitch_list("s c b b s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #11 Clay Buchholz
t7 = game.new_inning()

# 7. TOR #28 Colby Rasmus (X - X - X)
t7.new_ab()
t7.pitch_list("c b f b")
t7.out("G3-1")

# 8. TOR #1  Emilio Bonifácio (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("F9")

# 9. TOR #66 Munenori Kawasaki (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("G3-1")


# Bot 7th
# Pitching: TOR #56 Mark Buehrle
b7 = game.new_inning()

# 6. BOS #5  Jonny Gomes (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("G5-3")

# 7. BOS #16 Will Middlebrooks (X - X - X)
b7.new_ab()
b7.pitch_list("c b c b")
b7.out("G4-3")

# 8. BOS #7  Stephen Drew (X - X - X)
b7.new_ab()
b7.pitch_list("c b f b")
b7.out("G4-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #11 Clay Buchholz
t8 = game.new_inning()

# 1. TOR #53 Melky Cabrera (X - X - X)
t8.new_ab()
t8.pitch_list("b c")
t8.out("G6-3")

# 2. TOR #19 José Bautista (X - X - X)
t8.new_ab()
t8.pitch_list("f")
t8.hit(1)
t8.advance(2, "10 G1-3")

# 3. TOR #10 Edwin Encarnación (X - X - 19)
t8.new_ab()
t8.pitch_list("1 b c c")
t8.out("G1-3")

# 4. TOR #9  J.P. Arencibia (X - 19 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("b s s f b f f c")
t8.out("!K")


# Bot 8th
# Pitching: TOR #56 Mark Buehrle
b8 = game.new_inning()

# 9. BOS #3  David Ross (X - X - X)
b8.new_ab()
b8.pitch_list("c s b b f f f b d")
b8.reach("BB")
b8.advance(4, "2 3B")

# Pitching change (TOR): #38 Darren Oliver replaces #56 Mark Buehrle
b8.pitching_substitution(38)

# 1. BOS #2  Jacoby Ellsbury (X - X - 3)
b8.new_ab()
b8.pitch_list("f")
b8.hit(3, rbis=1)
b8.advance(4, "15 1B")

# 2. BOS #18 Shane Victorino (2 - X - X)
b8.new_ab(is_risp=True)
b8.pitch_list("c b f f s")
b8.out("K")

# 3. BOS #15 Dustin Pedroia (2 - X - X)
b8.new_ab(is_risp=True)
b8.pitch_list("f")
b8.hit(1, rbis=1)
b8.advance(2, "34 SB")

# 4. BOS #34 David Ortiz (X - X - 15)
b8.new_ab(is_risp=True)
b8.pitch_list("1 s b b s s")
b8.out("K")

# 5. BOS #12 Mike Napoli (X - 15 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("i i i i")
b8.reach("IBB")

# 6. BOS #5  Jonny Gomes (X - 15 - 12)
b8.new_ab(is_risp=True)
b8.pitch_list("f c c")
b8.out("!K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #36 Junichi Tazawa
t9 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #11 Clay Buchholz
t9.pitching_substitution(36)

# 5. TOR #26 Adam Lind (X - X - X)
t9.new_ab()
t9.pitch_list("c s b b f")
t9.hit(4)

# 6. TOR #13 Brett Lawrie (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.hit(1)
t9.thrown_out(2, "28 CS", 2, 36)

# 7. TOR #28 Colby Rasmus (X - X - 13)
t9.new_ab()
t9.pitch_list("f f f b d s")
t9.out("KDP2-6")

# 8. TOR #1  Emilio Bonifácio (X - X - X)
t9.new_ab()
t9.pitch_list("b c b f f b s")
t9.out("K")


# Bot 9th
# Pitching: TOR #44 Casey Janssen
b9 = game.new_inning()

# Pitching change (TOR): #44 Casey Janssen replaces #38 Darren Oliver
b9.pitching_substitution(44)

# 7. BOS #16 Will Middlebrooks (X - X - X)
b9.new_ab()
b9.pitch_list("c f b")
b9.hit(2)

# 8. BOS #7  Stephen Drew (X - 16 - X)
b9.new_ab(is_risp=True)
b9.pitch_list("b b")
b9.out("L6")

# Offensive change (BOS): Pinch-hitter #29 Daniel Nava replaces #3 David Ross, batting 9th
b9.offensive_substitution(9, 29, "PH")

# 9. BOS #29 Daniel Nava (X - 16 - X)
b9.new_ab(is_risp=True)
b9.pitch_list("f")
b9.out("F7")

# 1. BOS #2  Jacoby Ellsbury (X - 16 - X)
b9.new_ab(is_risp=True)
b9.out("G1-3")

# Winning team: TOR
# WP: TOR #38 Darren Oliver
game.winning_pitcher(38, is_away_team=True)
# SV: TOR #44 Casey Janssen
game.save_pitcher(44, is_away_team=True)

# Loser team: BOS
# LP: BOS #36 Junichi Tazawa
game.losing_pitcher(36)

# print(game)
game.generate_scorecard()
