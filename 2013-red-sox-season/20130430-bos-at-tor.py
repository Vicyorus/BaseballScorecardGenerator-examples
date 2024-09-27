import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TOR, 2013-04-30
# https://www.baseball-reference.com/boxes/TOR/TOR201304300.shtml
# https://www.mlb.com/gameday/red-sox-vs-blue-jays/2013/04/30/347142/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-04-30 19:08-22:22",
        "at": "Rogers Centre, Toronto, ON",
        "att": "22,915",
        "temp": "68F, Roof Closed",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                29: "Daniel Nava",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                37: "Mike Carp",
                39: "Jarrod Saltalamacchia",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                3: "David Ross",
                18: "Shane Victorino",
                23: "Pedro Ciriaco",
                5: "Jonny Gomes",
                # Bullpen
                63: "Alex Wilson",
                41: "John Lackey",
                30: "Andrew Miller",
                19: "Koji Uehara",
                52: "Joel Hanrahan",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
                11: "Clay Buchholz",
            },
            "lefties": [31, 30, 22],
            "lineup": [
                [2, "8"],
                [29, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [37, "7"],
                [39, "2"],
                [16, "5"],
                [7, "6"],
            ],
            "bench": [
                [3, "C"],
                [18, "CF"],
                [23, "3B"],
                [5, "LF"],
            ],
            "bullpen": [63, 41, 30, 19, 52, 59, 36, 22, 46, 11],
        },
        "home": {
            "team": "Toronto Blue Jays",
            "starter": 23,
            "roster": {
                # Lineup
                13: "Brett Lawrie",
                11: "Rajai Davis",
                19: "José Bautista",
                10: "Edwin Encarnación",
                53: "Melky Cabrera",
                9: "J.P. Arencibia",
                3: "Maicer Izturis",
                28: "Colby Rasmus",
                1: "Emilio Bonifácio",
                # Starting pitcher
                23: "Brandon Morrow",
                # Bench
                26: "Adam Lind",
                66: "Munenori Kawasaki",
                22: "Henry Blanco",
                16: "Mark DeRosa",
                # Bullpen
                43: "R.A. Dickey",
                52: "Justin Germano",
                62: "Aaron Loup",
                50: "Steve Delabar",
                56: "Mark Buehrle",
                27: "Brett Cecil",
                48: "J.A. Happ",
                44: "Casey Janssen",
                32: "Esmil Rogers",
                38: "Darren Oliver",
            },
            "lefties": [62, 56, 27, 48, 38],
            "lineup": [
                [13, "5"],
                [11, "0"],
                [19, "9"],
                [10, "3"],
                [53, "7"],
                [9, "2"],
                [3, "6"],
                [28, "8"],
                [1, "4"],
            ],
            "bench": [
                [26, "1B"],
                [66, "2B"],
                [22, "C"],
                [16, "3B"],
            ],
            "bullpen": [43, 52, 62, 50, 56, 27, 48, 44, 32, 38],
        },
        "umpires": {
            "HP": "Clint Fagan",
            "1B": "Bruce Dreckman",
            "2B": "Gary Darling",
            "3B": "Paul Emmel",
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
# Pitching: TOR #23 Brandon Morrow
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("b c b b s b")
t1.reach("BB")
t1.advance(2, "15 1B")

# 2. BOS #29 Daniel Nava (X - X - 2)
t1.new_ab()
t1.pitch_list("b c c b")
t1.out("F8")

# 3. BOS #15 Dustin Pedroia (X - X - 2)
t1.new_ab()
t1.pitch_list("c b")
t1.hit(1)

# 4. BOS #34 David Ortiz (X - 2 - 15)
t1.new_ab()
t1.pitch_list("t f s")
t1.out("K")

# 5. BOS #12 Mike Napoli (X - 2 - 15)
t1.new_ab()
t1.pitch_list("c s f d f f b f f s")
t1.out("K")


# Bot 1st
# Pitching: BOS #31 Jon Lester
b1 = game.new_inning()

# 1. TOR #13 Brett Lawrie (X - X - X)
b1.new_ab()
b1.pitch_list("b f")
b1.out("G6-3")

# 2. TOR #11 Rajai Davis (X - X - X)
b1.new_ab()
b1.pitch_list("b f b b b")
b1.reach("BB")
b1.advance(2, "19 SB")
b1.advance(4, "19 2B")

# 3. TOR #19 José Bautista (X - X - 11)
b1.new_ab()
b1.pitch_list("b")
b1.hit(2, rbis=1)

# 4. TOR #10 Edwin Encarnación (X - 19 - X)
b1.new_ab()
b1.pitch_list("b b f c d")
b1.out("F8")

# 5. TOR #53 Melky Cabrera (X - 19 - X)
b1.new_ab()
b1.pitch_list("f f f f s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TOR #23 Brandon Morrow
t2 = game.new_inning()

# 6. BOS #37 Mike Carp (X - X - X)
t2.new_ab()
t2.pitch_list("b s f s")
t2.out("K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t2.new_ab()
t2.pitch_list("c b t s")
t2.out("K")

# 8. BOS #16 Will Middlebrooks (X - X - X)
t2.new_ab()
t2.pitch_list("c s c")
t2.out("!K")


# Bot 2nd
# Pitching: BOS #31 Jon Lester
b2 = game.new_inning()

# 6. TOR #9  J.P. Arencibia (X - X - X)
b2.new_ab()
b2.pitch_list("c c b b")
b2.out("G5-3")

# 7. TOR #3  Maicer Izturis (X - X - X)
b2.new_ab()
b2.pitch_list("b c")
b2.out("L8")

# 8. TOR #28 Colby Rasmus (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.hit(1)

# 9. TOR #1  Emilio Bonifácio (X - X - 28)
b2.new_ab()
b2.pitch_list("b s f c")
b2.out("!K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TOR #23 Brandon Morrow
t3 = game.new_inning()

# 9. BOS #7  Stephen Drew (X - X - X)
t3.new_ab()
t3.pitch_list("b c b b")
t3.out("G3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.pitch_list("c b b b b")
t3.reach("BB")

# 2. BOS #29 Daniel Nava (X - X - 2)
t3.new_ab()
t3.pitch_list("b b c")
t3.out("F7")

# 3. BOS #15 Dustin Pedroia (X - X - 2)
t3.new_ab()
t3.pitch_list("b d f c f")
t3.out("L9")


# Bot 3rd
# Pitching: BOS #31 Jon Lester
b3 = game.new_inning()

# 1. TOR #13 Brett Lawrie (X - X - X)
b3.new_ab()
b3.pitch_list("b b")
b3.hit(1)
b3.advance(2, "11 HBP")
b3.advance(3, "19 BB")
b3.advance(4, "10 POE2")

# 2. TOR #11 Rajai Davis (X - X - 13)
b3.new_ab()
b3.pitch_list("b")
b3.reach("HBP")
b3.advance(2, "19 BB")
b3.advance(4, "10 POE2")

# 3. TOR #19 José Bautista (X - 13 - 11)
b3.new_ab()
b3.pitch_list("b b b b")
b3.reach("BB")
b3.error(2)
b3.advance(2, "10 POE2")
b3.advance(3, "10 F8")
b3.advance("U", "9 2B")

# 4. TOR #10 Edwin Encarnación (13 - 11 - 19)
b3.new_ab()
b3.pitch_list("b b c b 1")
b3.out("F8")

# 5. TOR #53 Melky Cabrera (19 - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("G4-3")

# 6. TOR #9  J.P. Arencibia (19 - X - X)
b3.new_ab()
b3.pitch_list("f")
b3.hit(2, rbis=1)

# 7. TOR #3  Maicer Izturis (X - 9 - X)
b3.new_ab()
b3.pitch_list("b c b s")
b3.out("P4")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TOR #23 Brandon Morrow
t4 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.hit(4)

# 5. BOS #12 Mike Napoli (X - X - X)
t4.new_ab()
t4.pitch_list("c b s b s")
t4.out("K")

# 6. BOS #37 Mike Carp (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.hit(4)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t4.new_ab()
t4.pitch_list("b b b c b")
t4.reach("BB")
t4.thrown_out(2, "16 DP5-4-3", 2, 23)

# 8. BOS #16 Will Middlebrooks (X - X - 39)
t4.new_ab()
t4.out("DP5-4-3")


# Bot 4th
# Pitching: BOS #31 Jon Lester
b4 = game.new_inning()

# 8. TOR #28 Colby Rasmus (X - X - X)
b4.new_ab()
b4.pitch_list("c f b f s")
b4.out("K")

# 9. TOR #1  Emilio Bonifácio (X - X - X)
b4.new_ab()
b4.pitch_list("b c f f s")
b4.out("K")

# 1. TOR #13 Brett Lawrie (X - X - X)
b4.new_ab()
b4.out("G1-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TOR #23 Brandon Morrow
t5 = game.new_inning()

# 9. BOS #7  Stephen Drew (X - X - X)
t5.new_ab()
t5.pitch_list("c b b f f f b")
t5.hit(1)
t5.advance(2, "2 1B")
t5.advance(4, "15 1B")

# 1. BOS #2  Jacoby Ellsbury (X - X - 7)
t5.new_ab()
t5.hit(1)
t5.advance(2, "15 1B")
t5.thrown_out(3, "12 POCS", 3, 23)

# 2. BOS #29 Daniel Nava (X - 7 - 2)
t5.new_ab()
t5.pitch_list("b f f f")
t5.out("F8")

# 3. BOS #15 Dustin Pedroia (X - 7 - 2)
t5.new_ab()
t5.pitch_list("c f f")
t5.hit(1, rbis=1)

# 4. BOS #34 David Ortiz (X - 2 - 15)
t5.new_ab()
t5.pitch_list("b s s s")
t5.out("K")

# 5. BOS #12 Mike Napoli (X - 2 - 15)
t5.new_ab()
t5.pitch_list("b 2")
t5.no_ab("POCS")


# Bot 5th
# Pitching: BOS #31 Jon Lester
b5 = game.new_inning()

# 2. TOR #11 Rajai Davis (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.hit(1)
b5.advance(4, "10 HR")

# 3. TOR #19 José Bautista (X - X - 11)
b5.new_ab()
b5.pitch_list("1 1 p f 1")
b5.out("F7")

# 4. TOR #10 Edwin Encarnación (X - X - 11)
b5.new_ab()
b5.pitch_list("1 b b b c")
b5.hit(4, rbis=2)

# 5. TOR #53 Melky Cabrera (X - X - X)
b5.new_ab()
b5.pitch_list("f")
b5.out("G6-3")

# 6. TOR #9  J.P. Arencibia (X - X - X)
b5.new_ab()
b5.pitch_list("b f s b b")
b5.out("G4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TOR #62 Aaron Loup
t6 = game.new_inning()

# Pitching change (TOR): #62 Aaron Loup replaces #23 Brandon Morrow
t6.pitching_substitution(62)

# 5. BOS #12 Mike Napoli (X - X - X)
t6.new_ab()
t6.pitch_list("c b c b c")
t6.out("!K")

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #37 Mike Carp, batting 6th
t6.offensive_substitution(6, 5, "PH")

# 6. BOS #5  Jonny Gomes (X - X - X)
t6.new_ab()
t6.pitch_list("c b f f b")
t6.hit(4)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t6.new_ab()
t6.pitch_list("c f b")
t6.out("G5-3")

# 8. BOS #16 Will Middlebrooks (X - X - X)
t6.new_ab()
t6.pitch_list("b s s b b")
t6.out("F7")


# Bot 6th
# Pitching: BOS #31 Jon Lester
b6 = game.new_inning()

# Defensive switch (BOS): #5 Jonny Gomes moves to LF
b6.defensive_switch(5, "7")

# 7. TOR #3  Maicer Izturis (X - X - X)
b6.new_ab()
b6.pitch_list("b b")
b6.out("F9")

# 8. TOR #28 Colby Rasmus (X - X - X)
b6.new_ab()
b6.pitch_list("f b b f s")
b6.out("K")

# 9. TOR #1  Emilio Bonifácio (X - X - X)
b6.new_ab()
b6.pitch_list("f b f b")
b6.out("G3-1")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TOR #62 Aaron Loup
t7 = game.new_inning()

# Defensive switch (TOR): #3 Maicer Izturis moves to 2B
t7.defensive_switch(3, "4")

# Defensive change (TOR): #66 Munenori Kawasaki replaces #1 Emilio Bonifácio (2B), playing SS, batting 9th
t7.defensive_substitution(9, 66, "6")

# 9. BOS #7  Stephen Drew (X - X - X)
t7.new_ab()
t7.pitch_list("b s f s")
t7.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t7.new_ab()
t7.pitch_list("c b c")
t7.hit(1)
t7.error(6)
t7.advance(2, "29 FC6")
t7.advance(3, "29 E6")
t7.advance("U", "34 2B")

# 2. BOS #29 Daniel Nava (X - X - 2)
t7.new_ab()
t7.reach("FC6")
t7.advance(2, "15 BB")
t7.advance(4, "34 2B")

# Pitching change (TOR): #50 Steve Delabar replaces #62 Aaron Loup
t7.pitching_substitution(50)

# 3. BOS #15 Dustin Pedroia (2 - X - 29)
t7.new_ab()
t7.pitch_list("b f b b f b")
t7.reach("BB")
t7.advance(4, "34 2B")

# 4. BOS #34 David Ortiz (2 - 29 - 15)
t7.new_ab()
t7.pitch_list("d f b b")
t7.hit(2, rbis=3)

# 5. BOS #12 Mike Napoli (X - 34 - X)
t7.new_ab()
t7.pitch_list("b s b c f d s")
t7.out("K")

# 6. BOS #5  Jonny Gomes (X - 34 - X)
t7.new_ab()
t7.pitch_list("b s d s")
t7.out("F9")


# Bot 7th
# Pitching: BOS #36 Junichi Tazawa
b7 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #31 Jon Lester
b7.pitching_substitution(36)

# 1. TOR #13 Brett Lawrie (X - X - X)
b7.new_ab()
b7.pitch_list("b s c")
b7.out("F8")

# Offensive change (TOR): Pinch-hitter #26 Adam Lind replaces #11 Rajai Davis, batting 2nd
b7.offensive_substitution(2, 26, "PH")

# 2. TOR #26 Adam Lind (X - X - X)
b7.new_ab()
b7.pitch_list("b f b b c s")
b7.out("K")

# 3. TOR #19 José Bautista (X - X - X)
b7.new_ab()
b7.pitch_list("f b c b b b")
b7.reach("BB")
b7.advance(4, "10 HR")

# 4. TOR #10 Edwin Encarnación (X - X - 19)
b7.new_ab()
b7.pitch_list("b c b")
b7.hit(4, rbis=2)

# 5. TOR #53 Melky Cabrera (X - X - X)
b7.new_ab()
b7.pitch_list("b f c s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TOR #38 Darren Oliver
t8 = game.new_inning()

# Pitching change (TOR): #38 Darren Oliver replaces #50 Steve Delabar
t8.pitching_substitution(38)

# Defensive switch (TOR): #26 Adam Lind moves to DH
t8.defensive_switch(26, "0")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t8.new_ab()
t8.pitch_list("b f c f f b b b")
t8.reach("BB")
t8.thrown_out(2, "7 FC6-4", 2, 38)

# 8. BOS #16 Will Middlebrooks (X - X - 39)
t8.new_ab()
t8.pitch_list("c f d b c")
t8.out("!K")

# 9. BOS #7  Stephen Drew (X - X - 39)
t8.new_ab()
t8.pitch_list("1 b b d c f")
t8.reach("FC6-4")

# 1. BOS #2  Jacoby Ellsbury (X - X - 7)
t8.new_ab()
t8.pitch_list("c c 1 b d f")
t8.out("G1-3")


# Bot 8th
# Pitching: BOS #52 Joel Hanrahan
b8 = game.new_inning()

# Pitching change (BOS): #52 Joel Hanrahan replaces #36 Junichi Tazawa
b8.pitching_substitution(52)

# 6. TOR #9  J.P. Arencibia (X - X - X)
b8.new_ab()
b8.pitch_list("f")
b8.hit(1)
b8.advance(2, "3 SAC1-4")
b8.advance(4, "28 1B")

# 7. TOR #3  Maicer Izturis (X - X - 9)
b8.new_ab()
b8.out("SAC1-4")

# 8. TOR #28 Colby Rasmus (X - 9 - X)
b8.new_ab()
b8.pitch_list("b b c f b")
b8.hit(1, rbis=1)
b8.advance(2, "66 G4-3")

# 9. TOR #66 Munenori Kawasaki (X - X - 28)
b8.new_ab()
b8.pitch_list("1 b f")
b8.out("G4-3")

# 1. TOR #13 Brett Lawrie (X - 28 - X)
b8.new_ab()
b8.pitch_list("c b b b")
b8.out("F8")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TOR #44 Casey Janssen
t9 = game.new_inning()

# Pitching change (TOR): #44 Casey Janssen replaces #38 Darren Oliver
t9.pitching_substitution(44)

# 2. BOS #29 Daniel Nava (X - X - X)
t9.new_ab()
t9.pitch_list("b c c")
t9.out("G5-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t9.new_ab()
t9.pitch_list("b f f b b")
t9.out("G6-3")

# 4. BOS #34 David Ortiz (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("F8")

# Winning team: TOR
# WP: TOR #50 Steve Delabar
game.winning_pitcher(50)
# SV: TOR #44 Casey Janssen
game.save_pitcher(44)

# Loser team: BOS
# LP: BOS #36 Junichi Tazawa
game.losing_pitcher(36, is_away_team=True)

# print(game)
game.generate_scorecard()
