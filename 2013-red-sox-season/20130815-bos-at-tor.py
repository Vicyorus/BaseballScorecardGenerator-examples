import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TOR, 2013-08-15
# https://www.baseball-reference.com/boxes/TOR/TOR201308150.shtml
# https://www.mlb.com/gameday/red-sox-vs-blue-jays/2013/08/15/348552/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-08-15 19:08-21:51",
        "at": "Rogers Centre, Toronto, ON",
        "att": "40,477",
        "temp": "68F, Partly Cloudy",
        "wind": "11mph, L To R",
        "away": {
            "team": "Boston Red Sox",
            "starter": 44,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                5: "Jonny Gomes",
                7: "Stephen Drew",
                20: "Ryan Lavarnway",
                29: "Daniel Nava",
                16: "Will Middlebrooks",
                # Starting pitcher
                44: "Jake Peavy",
                # Bench
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                26: "Brock Holt",
                12: "Mike Napoli",
                # Bullpen
                41: "John Lackey",
                67: "Brandon Workman",
                56: "Franklin Morales",
                32: "Craig Breslow",
                66: "Drake Britton",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                62: "Rubby De La Rosa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [56, 32, 66, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [5, "7"],
                [7, "6"],
                [20, "2"],
                [29, "3"],
                [16, "5"],
            ],
            "bench": [
                [39, "C"],
                [37, "1B"],
                [26, "2B"],
                [12, "1B"],
            ],
            "bullpen": [41, 67, 56, 32, 66, 31, 36, 19, 62, 22, 46],
        },
        "home": {
            "team": "Toronto Blue Jays",
            "starter": 56,
            "roster": {
                # Lineup
                7: "José Reyes",
                11: "Rajai Davis",
                19: "José Bautista",
                10: "Edwin Encarnación",
                13: "Brett Lawrie",
                26: "Adam Lind",
                9: "J.P. Arencibia",
                22: "Kevin Pillar",
                66: "Munenori Kawasaki",
                # Starting pitcher
                56: "Mark Buehrle",
                # Bench
                3: "Maicer Izturis",
                16: "Mark DeRosa",
                22: "Josh Thole",
                # Bullpen
                43: "R.A. Dickey",
                45: "Neil Wagner",
                62: "Aaron Loup",
                51: "Thad Weber",
                37: "Mickey Storey",
                38: "Darren Oliver",
                58: "Todd Redmond",
                49: "Brad Lincoln",
                27: "Brett Cecil",
                21: "Sergio Santos",
                44: "Casey Janssen",
                32: "Esmil Rogers",
            },
            "lefties": [56, 62, 38, 27],
            "lineup": [
                [7, "6"],
                [11, "8"],
                [19, "9"],
                [10, "0"],
                [13, "5"],
                [26, "3"],
                [9, "2"],
                [22, "7"],
                [66, "4"],
            ],
            "bench": [
                [3, "3B"],
                [16, "3B"],
                [22, "C"],
            ],
            "bullpen": [43, 45, 62, 51, 37, 38, 58, 49, 27, 21, 44, 32],
        },
        "umpires": {
            "HP": "Chris Guccione",
            "1B": "John Tumpane",
            "2B": "Tom Hallion",
            "3B": "Phil Cuzzi",
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
# Pitching: TOR #56 Mark Buehrle
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.out("F8")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("c s b s")
t1.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("c f b")
t1.hit(1)
t1.advance(2, "34 BB")
t1.advance(3, "5 1B")
t1.thrown_out(4, "5 7-2", 3, 56)

# 4. BOS #34 David Ortiz (X - X - 15)
t1.new_ab()
t1.pitch_list("f b b b 1 b")
t1.reach("BB")
t1.advance(2, "5 7-2")

# 5. BOS #5  Jonny Gomes (X - 15 - 34)
t1.new_ab(is_risp=True)
t1.pitch_list("c")
t1.hit(1)


# Bot 1st
# Pitching: BOS #44 Jake Peavy
b1 = game.new_inning()

# 1. TOR #7  José Reyes (X - X - X)
b1.new_ab()
b1.pitch_list("c f b")
b1.out("G4-3")

# 2. TOR #11 Rajai Davis (X - X - X)
b1.new_ab()
b1.pitch_list("b f f f b f b f")
b1.out("F8")

# 3. TOR #19 José Bautista (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("F7")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TOR #56 Mark Buehrle
t2 = game.new_inning()

# 6. BOS #7  Stephen Drew (X - X - X)
t2.new_ab()
t2.pitch_list("b f f f b b f")
t2.out("L4")

# 7. BOS #20 Ryan Lavarnway (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.hit(1)
t2.advance(2, "29 1B")
t2.advance(3, "2 BB")

# 8. BOS #29 Daniel Nava (X - X - 20)
t2.new_ab()
t2.pitch_list("c")
t2.hit(1)
t2.advance(2, "2 BB")

# 9. BOS #16 Will Middlebrooks (X - 20 - 29)
t2.new_ab(is_risp=True)
t2.pitch_list("c d")
t2.out("L8")

# 1. BOS #2  Jacoby Ellsbury (X - 20 - 29)
t2.new_ab(is_risp=True)
t2.pitch_list("b b c c b d")
t2.reach("BB")

# 2. BOS #18 Shane Victorino (20 - 29 - 2)
t2.new_ab(is_risp=True)
t2.pitch_list("c")
t2.out("L9")


# Bot 2nd
# Pitching: BOS #44 Jake Peavy
b2 = game.new_inning()

# 4. TOR #10 Edwin Encarnación (X - X - X)
b2.new_ab()
b2.pitch_list("c b f")
b2.out("F8")

# 5. TOR #13 Brett Lawrie (X - X - X)
b2.new_ab()
b2.out("(F)P3")

# 6. TOR #26 Adam Lind (X - X - X)
b2.new_ab()
b2.pitch_list("c c f b")
b2.hit(2)

# 7. TOR #9  J.P. Arencibia (X - 26 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("c t b b d s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TOR #56 Mark Buehrle
t3 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t3.new_ab()
t3.hit(1)
t3.advance(3, "34 G5-3")

# 4. BOS #34 David Ortiz (X - X - 15)
t3.new_ab()
t3.pitch_list("f")
t3.out("G5-3")

# 5. BOS #5  Jonny Gomes (15 - X - X)
t3.new_ab(is_risp=True)
t3.pitch_list("c")
t3.out("(F)P5")

# 6. BOS #7  Stephen Drew (15 - X - X)
t3.new_ab(is_risp=True)
t3.pitch_list("c b s s")
t3.out("K")


# Bot 3rd
# Pitching: BOS #44 Jake Peavy
b3 = game.new_inning()

# 8. TOR #22 Kevin Pillar (X - X - X)
b3.new_ab()
b3.pitch_list("b s s s")
b3.out("K")

# 9. TOR #66 Munenori Kawasaki (X - X - X)
b3.new_ab()
b3.pitch_list("b b c f f b f")
b3.out("L9")

# 1. TOR #7  José Reyes (X - X - X)
b3.new_ab()
b3.pitch_list("c s b f b b f")
b3.out("F8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TOR #56 Mark Buehrle
t4 = game.new_inning()

# 7. BOS #20 Ryan Lavarnway (X - X - X)
t4.new_ab()
t4.pitch_list("b b b c")
t4.out("F9")

# 8. BOS #29 Daniel Nava (X - X - X)
t4.new_ab()
t4.pitch_list("b c c b f")
t4.hit(2)
t4.advance(3, "16 1B")
t4.advance(4, "2 FC4-6")

# 9. BOS #16 Will Middlebrooks (X - 29 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b c c")
t4.hit(1)
t4.thrown_out(2, "2 FC4-6", 2, 56)

# 1. BOS #2  Jacoby Ellsbury (29 - X - 16)
t4.new_ab(is_risp=True)
t4.pitch_list("f 1 1 b f b f b 1")
t4.reach("FC4-6", rbis=1)

# 2. BOS #18 Shane Victorino (X - X - 2)
t4.new_ab()
t4.pitch_list("1 t 1 1")
t4.out("P5")


# Bot 4th
# Pitching: BOS #44 Jake Peavy
b4 = game.new_inning()

# 2. TOR #11 Rajai Davis (X - X - X)
b4.new_ab()
b4.pitch_list("c f b c")
b4.out("!K")

# 3. TOR #19 José Bautista (X - X - X)
b4.new_ab()
b4.pitch_list("b b c c")
b4.out("G1-3")

# 4. TOR #10 Edwin Encarnación (X - X - X)
b4.new_ab()
b4.pitch_list("c b f b")
b4.out("P4")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TOR #56 Mark Buehrle
t5 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("F8")

# 4. BOS #34 David Ortiz (X - X - X)
t5.new_ab()
t5.pitch_list("b b f")
t5.out("F8")

# 5. BOS #5  Jonny Gomes (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("G5-3")


# Bot 5th
# Pitching: BOS #44 Jake Peavy
b5 = game.new_inning()

# 5. TOR #13 Brett Lawrie (X - X - X)
b5.new_ab()
b5.pitch_list("b b f f f")
b5.out("L8")

# 6. TOR #26 Adam Lind (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.out("G6-3")

# 7. TOR #9  J.P. Arencibia (X - X - X)
b5.new_ab()
b5.pitch_list("c s")
b5.hit(1)

# 8. TOR #22 Kevin Pillar (X - X - 9)
b5.new_ab()
b5.pitch_list("c 1 s s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TOR #56 Mark Buehrle
t6 = game.new_inning()

# 6. BOS #7  Stephen Drew (X - X - X)
t6.new_ab()
t6.pitch_list("f b")
t6.hit(1)
t6.advance(3, "20 1B")

# 7. BOS #20 Ryan Lavarnway (X - X - 7)
t6.new_ab()
t6.hit(1)

# 8. BOS #29 Daniel Nava (7 - X - 20)
t6.new_ab(is_risp=True)
t6.pitch_list("c f f s")
t6.out("K")

# 9. BOS #16 Will Middlebrooks (7 - X - 20)
t6.new_ab(is_risp=True)
t6.pitch_list("s b c d t")
t6.out("KT")

# 1. BOS #2  Jacoby Ellsbury (7 - X - 20)
t6.new_ab(is_risp=True)
t6.pitch_list("f f")
t6.out("G5-3")


# Bot 6th
# Pitching: BOS #44 Jake Peavy
b6 = game.new_inning()

# 9. TOR #66 Munenori Kawasaki (X - X - X)
b6.new_ab()
b6.pitch_list("b c b c")
b6.out("G6-3")

# 1. TOR #7  José Reyes (X - X - X)
b6.new_ab()
b6.pitch_list("f")
b6.out("F7")

# 2. TOR #11 Rajai Davis (X - X - X)
b6.new_ab()
b6.pitch_list("s")
b6.out("F9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TOR #56 Mark Buehrle
t7 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
t7.new_ab()
t7.out("G4-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t7.new_ab()
t7.pitch_list("b b c")
t7.hit(1)

# 4. BOS #34 David Ortiz (X - X - 15)
t7.new_ab()
t7.pitch_list("b c b b")
t7.out("L8")

# 5. BOS #5  Jonny Gomes (X - X - 15)
t7.new_ab()
t7.pitch_list("b b")
t7.out("F8")


# Bot 7th
# Pitching: BOS #44 Jake Peavy
b7 = game.new_inning()

# 3. TOR #19 José Bautista (X - X - X)
b7.new_ab()
b7.pitch_list("c b b b f")
b7.hit(1)
b7.advance(2, "10 1B")
b7.advance(4, "13 1B")

# 4. TOR #10 Edwin Encarnación (X - X - 19)
b7.new_ab()
b7.pitch_list("b")
b7.hit(1)
b7.advance(3, "13 1B")
b7.advance(4, "16 SF8")

# 5. TOR #13 Brett Lawrie (X - 19 - 10)
b7.new_ab(is_risp=True)
b7.pitch_list("f")
b7.hit(1, rbis=1)

# Pitching change (BOS): #32 Craig Breslow replaces #44 Jake Peavy
b7.pitching_substitution(32)

# Offensive change (TOR): Pinch-hitter #16 Mark DeRosa replaces #26 Adam Lind, batting 6th
b7.offensive_substitution(6, 16, "PH")

# 6. TOR #16 Mark DeRosa (10 - X - 13)
b7.new_ab(is_risp=True)
b7.pitch_list("1 b b f b")
b7.out("SF8", rbis=1)

# 7. TOR #9  J.P. Arencibia (X - X - 13)
b7.new_ab()
b7.pitch_list("f b b f b")
b7.out("F9")

# 8. TOR #22 Kevin Pillar (X - X - 13)
b7.new_ab()
b7.pitch_list("b b f s s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TOR #38 Darren Oliver
t8 = game.new_inning()

# Pitching change (TOR): #38 Darren Oliver replaces #56 Mark Buehrle
t8.pitching_substitution(38)

# Defensive switch (TOR): #16 Mark DeRosa moves to 1B
t8.defensive_switch(16, "3")

# 6. BOS #7  Stephen Drew (X - X - X)
t8.new_ab()
t8.pitch_list("b s c b")
t8.out("G5-3")

# 7. BOS #20 Ryan Lavarnway (X - X - X)
t8.new_ab()
t8.pitch_list("b c b f b")
t8.out("G6-3")

# 8. BOS #29 Daniel Nava (X - X - X)
t8.new_ab()
t8.pitch_list("c b b f b")
t8.hit(2)

# 9. BOS #16 Will Middlebrooks (X - 29 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("b s f b d b")
t8.reach("BB")

# 1. BOS #2  Jacoby Ellsbury (X - 29 - 16)
t8.new_ab(is_risp=True)
t8.pitch_list("c f b s")
t8.out("K")


# Bot 8th
# Pitching: BOS #36 Junichi Tazawa
b8 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #32 Craig Breslow
b8.pitching_substitution(36)

# 9. TOR #66 Munenori Kawasaki (X - X - X)
b8.new_ab()
b8.pitch_list("c c")
b8.out("G3")

# 1. TOR #7  José Reyes (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("G4-3")

# 2. TOR #11 Rajai Davis (X - X - X)
b8.new_ab()
b8.pitch_list("b s b b c")
b8.hit(1)
b8.error(2)
b8.advance(2, "19 SB")
b8.advance(3, "19 E2")

# Pitching change (BOS): #62 Rubby De La Rosa replaces #36 Junichi Tazawa
b8.pitching_substitution(62)

# 3. TOR #19 José Bautista (X - X - 11)
b8.new_ab(is_risp=True)
b8.pitch_list("1 b b b")
b8.out("G6-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TOR #44 Casey Janssen
t9 = game.new_inning()

# Pitching change (TOR): #44 Casey Janssen replaces #38 Darren Oliver
t9.pitching_substitution(44)

# 2. BOS #18 Shane Victorino (X - X - X)
t9.new_ab()
t9.pitch_list("c b f b f")
t9.out("G4-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t9.new_ab()
t9.pitch_list("c b")
t9.out("L9")

# 4. BOS #34 David Ortiz (X - X - X)
t9.new_ab()
t9.pitch_list("b c b b f")
t9.out("F8")

# Winning team: TOR
# WP: TOR #56 Mark Buehrle
game.winning_pitcher(56)
# SV: TOR #44 Casey Janssen
game.save_pitcher(44)

# Loser team: BOS
# LP: BOS #44 Jake Peavy
game.losing_pitcher(44, is_away_team=True)

# print(game)
game.generate_scorecard()
