import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ HOU, 2013-08-05
# https://www.baseball-reference.com/boxes/HOU/HOU201308050.shtml
# https://www.mlb.com/gameday/red-sox-vs-astros/2013/08/05/348413/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-08-05 20:12-23:23",
        "at": "Minute Maid Park, Houston, TX",
        "att": "24,539",
        "temp": "73F, Roof Closed",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                5: "Jonny Gomes",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                23: "Brandon Snyder",
                # Starting pitcher
                41: "John Lackey",
                # Bench
                37: "Mike Carp",
                26: "Brock Holt",
                20: "Ryan Lavarnway",
                # Bullpen
                35: "Steven Wright",
                67: "Brandon Workman",
                32: "Craig Breslow",
                19: "Koji Uehara",
                66: "Drake Britton",
                44: "Jake Peavy",
                62: "Rubby De La Rosa",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [32, 66, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [5, "7"],
                [39, "2"],
                [7, "6"],
                [23, "5"],
            ],
            "bench": [
                [37, "1B"],
                [26, "2B"],
                [20, "C"],
            ],
            "bullpen": [35, 67, 32, 19, 66, 44, 62, 31, 36, 22, 46],
        },
        "home": {
            "team": "Houston Astros",
            "starter": 39,
            "roster": {
                # Lineup
                19: "Robbie Grossman",
                2: "Brandon Barnes",
                27: "Jose Altuve",
                15: "Jason Castro",
                23: "Chris Carter",
                29: "Brett Wallace",
                30: "Matt Dominguez",
                28: "L.J. Hoes",
                6: "Jonathan Villar",
                # Starting pitcher
                39: "Brett Oberholtzer",
                # Bench
                10: "Jake Elmore",
                59: "Marc Krauss",
                22: "Carlos Corporán",
                # Bullpen
                45: "Erik Bedard",
                53: "Wesley Wright",
                63: "Chia-Jen Lo",
                64: "Lucas Harrell",
                35: "Josh Fields",
                54: "Travis Blackley",
                60: "Dallas Keuchel",
                48: "Jarred Cosart",
                41: "Brad Peacock",
                68: "José Cisnero",
                18: "Jordan Lyles",
                61: "Josh Zeid",
            },
            "lefties": [39, 45, 53, 54, 60],
            "lineup": [
                [19, "7"],
                [2, "8"],
                [27, "4"],
                [15, "2"],
                [23, "0"],
                [29, "3"],
                [30, "5"],
                [28, "9"],
                [6, "6"],
            ],
            "bench": [
                [10, "2B"],
                [59, "1B"],
                [22, "C"],
            ],
            "bullpen": [45, 53, 63, 64, 35, 54, 60, 48, 41, 68, 18, 61],
        },
        "umpires": {
            "HP": "Dan Iassogna",
            "1B": "Brian Knight",
            "2B": "Mark Carlson",
            "3B": "Gerry Davis",
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
# Pitching: HOU #39 Brett Oberholtzer
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.out("F8")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("b b")
t1.out("P4")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.out("G6-3")


# Bot 1st
# Pitching: BOS #41 John Lackey
b1 = game.new_inning()

# 1. HOU #19 Robbie Grossman (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("F8")

# 2. HOU #2  Brandon Barnes (X - X - X)
b1.new_ab()
b1.pitch_list("c b b")
b1.out("G5-3")

# 3. HOU #27 Jose Altuve (X - X - X)
b1.new_ab()
b1.pitch_list("c b b")
b1.out("G6-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: HOU #39 Brett Oberholtzer
t2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t2.new_ab()
t2.pitch_list("b b")
t2.error(3)
t2.reach("E3")
t2.advance(2, "39 BB")

# 5. BOS #12 Mike Napoli (X - X - 34)
t2.new_ab()
t2.pitch_list("c b b s b f f")
t2.out("F9")

# 6. BOS #5  Jonny Gomes (X - X - 34)
t2.new_ab()
t2.pitch_list("c f")
t2.out("(F)P3")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 34)
t2.new_ab()
t2.pitch_list("b b c d b")
t2.reach("BB")

# 8. BOS #7  Stephen Drew (X - 34 - 39)
t2.new_ab(is_risp=True)
t2.pitch_list("b f")
t2.out("P6")


# Bot 2nd
# Pitching: BOS #41 John Lackey
b2 = game.new_inning()

# 4. HOU #15 Jason Castro (X - X - X)
b2.new_ab()
b2.pitch_list("b f c b f f")
b2.out("G3")

# 5. HOU #23 Chris Carter (X - X - X)
b2.new_ab()
b2.pitch_list("b s s s")
b2.out("K")

# 6. HOU #29 Brett Wallace (X - X - X)
b2.new_ab()
b2.pitch_list("f b b")
b2.hit(2)

# 7. HOU #30 Matt Dominguez (X - 29 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("c")
b2.out("G1-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: HOU #39 Brett Oberholtzer
t3 = game.new_inning()

# 9. BOS #23 Brandon Snyder (X - X - X)
t3.new_ab()
t3.pitch_list("c b b")
t3.out("L6")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.pitch_list("c f")
t3.out("G5-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("L4")


# Bot 3rd
# Pitching: BOS #41 John Lackey
b3 = game.new_inning()

# 8. HOU #28 L.J. Hoes (X - X - X)
b3.new_ab()
b3.pitch_list("b s b")
b3.out("L3")

# 9. HOU #6  Jonathan Villar (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.hit(1)
b3.advance(2, "19 SB")
b3.advance(3, "2 SB")

# 1. HOU #19 Robbie Grossman (X - X - 6)
b3.new_ab(is_risp=True)
b3.pitch_list("1 b b s f s")
b3.out("K")

# 2. HOU #2  Brandon Barnes (X - 6 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("d c b s f f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: HOU #39 Brett Oberholtzer
t4 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t4.new_ab()
t4.pitch_list("b b b c f")
t4.hit(1)
t4.thrown_out(2, "5 CS", 3, 39)

# 4. BOS #34 David Ortiz (X - X - 15)
t4.new_ab()
t4.pitch_list("1 b f s")
t4.out("F8")

# 5. BOS #12 Mike Napoli (X - X - 15)
t4.new_ab()
t4.pitch_list("t 1 1 s")
t4.out("F9")

# 6. BOS #5  Jonny Gomes (X - X - 15)
t4.new_ab()
t4.pitch_list("s 1 c")
t4.no_ab("CS")


# Bot 4th
# Pitching: BOS #41 John Lackey
b4 = game.new_inning()

# 3. HOU #27 Jose Altuve (X - X - X)
b4.new_ab()
b4.pitch_list("b b c c")
b4.hit(1)
b4.advance(2, "15 SB")
b4.thrown_out(3, "29 CS", 2, 41)

# 4. HOU #15 Jason Castro (X - X - 27)
b4.new_ab(is_risp=True)
b4.pitch_list("1 b f b s b b")
b4.reach("BB")

# 5. HOU #23 Chris Carter (X - 27 - 15)
b4.new_ab(is_risp=True)
b4.pitch_list("s d f b s")
b4.out("K")

# 6. HOU #29 Brett Wallace (X - 27 - 15)
b4.new_ab()
b4.pitch_list("s c b c")
b4.out("!K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: HOU #39 Brett Oberholtzer
t5 = game.new_inning()

# 6. BOS #5  Jonny Gomes (X - X - X)
t5.new_ab()
t5.pitch_list("f c b")
t5.out("F8")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("F9")

# 8. BOS #7  Stephen Drew (X - X - X)
t5.new_ab()
t5.pitch_list("b b b c")
t5.hit(2)

# 9. BOS #23 Brandon Snyder (X - 7 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("s")
t5.out("F8")


# Bot 5th
# Pitching: BOS #41 John Lackey
b5 = game.new_inning()

# 7. HOU #30 Matt Dominguez (X - X - X)
b5.new_ab()
b5.pitch_list("c f f b s")
b5.out("K")

# 8. HOU #28 L.J. Hoes (X - X - X)
b5.new_ab()
b5.pitch_list("f")
b5.hit(1)
b5.advance(2, "6 SB")
b5.advance(4, "19 1B")

# 9. HOU #6  Jonathan Villar (X - X - 28)
b5.new_ab(is_risp=True)
b5.pitch_list("b 1 1 s c b b b")
b5.reach("BB")
b5.advance(3, "19 1B")

# 1. HOU #19 Robbie Grossman (X - 28 - 6)
b5.new_ab(is_risp=True)
b5.hit(1, rbis=1)
b5.advance(2, "2 SB")

# 2. HOU #2  Brandon Barnes (6 - X - 19)
b5.new_ab(is_risp=True)
b5.pitch_list("m s f b s")
b5.out("K")

# 3. HOU #27 Jose Altuve (6 - 19 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("f c t")
b5.out("KT")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: HOU #39 Brett Oberholtzer
t6 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t6.new_ab()
t6.pitch_list("c s")
t6.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t6.new_ab()
t6.pitch_list("c b b b f f")
t6.out("G5-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.hit(1)
t6.advance(2, "34 BB")

# 4. BOS #34 David Ortiz (X - X - 15)
t6.new_ab()
t6.pitch_list("b b f b f d")
t6.reach("BB")
t6.thrown_out(2, "12 FC4", 3, 39)

# 5. BOS #12 Mike Napoli (X - 15 - 34)
t6.new_ab(is_risp=True)
t6.pitch_list("b")
t6.reach("FC4")


# Bot 6th
# Pitching: BOS #41 John Lackey
b6 = game.new_inning()

# 4. HOU #15 Jason Castro (X - X - X)
b6.new_ab()
b6.pitch_list("b c b")
b6.hit(1)
b6.thrown_out(2, "30 FC6-4", 3, 41)

# 5. HOU #23 Chris Carter (X - X - 15)
b6.new_ab()
b6.pitch_list("b c b s b f f s")
b6.out("K")

# 6. HOU #29 Brett Wallace (X - X - 15)
b6.new_ab()
b6.pitch_list("b s b s s")
b6.out("K")

# 7. HOU #30 Matt Dominguez (X - X - 15)
b6.new_ab()
b6.pitch_list("s f")
b6.reach("FC6-4")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: HOU #39 Brett Oberholtzer
t7 = game.new_inning()

# 6. BOS #5  Jonny Gomes (X - X - X)
t7.new_ab()
t7.pitch_list("c b")
t7.hit(2)
t7.advance(3, "39 F9")

# 7. BOS #39 Jarrod Saltalamacchia (X - 5 - X)
t7.new_ab(is_risp=True)
t7.out("F9")

# 8. BOS #7  Stephen Drew (5 - X - X)
t7.new_ab(is_risp=True)
t7.pitch_list("b c f s")
t7.out("K")

# 9. BOS #23 Brandon Snyder (5 - X - X)
t7.new_ab(is_risp=True)
t7.pitch_list("d f f s")
t7.out("K")


# Bot 7th
# Pitching: BOS #41 John Lackey
b7 = game.new_inning()

# 8. HOU #28 L.J. Hoes (X - X - X)
b7.new_ab()
b7.pitch_list("b b c f")
b7.hit(2)
b7.advance(3, "6 1B")
b7.advance(4, "2 SAC1-3")

# 9. HOU #6  Jonathan Villar (X - 28 - X)
b7.new_ab(is_risp=True)
b7.hit(1)
b7.advance(2, "2 SB")
b7.advance(3, "2 SAC1-3")

# Pitching change (BOS): #36 Junichi Tazawa replaces #41 John Lackey
b7.pitching_substitution(36)

# 1. HOU #19 Robbie Grossman (28 - X - 6)
b7.new_ab(is_risp=True)
b7.pitch_list("l s d c")
b7.out("!K")

# 2. HOU #2  Brandon Barnes (28 - X - 6)
b7.new_ab(is_risp=True)
b7.pitch_list("b")
b7.out("SAC1-3", rbis=1)

# 3. HOU #27 Jose Altuve (6 - X - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b")
b7.out("G6-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: HOU #53 Wesley Wright
t8 = game.new_inning()

# Pitching change (HOU): #53 Wesley Wright replaces #39 Brett Oberholtzer
t8.pitching_substitution(53)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t8.new_ab()
t8.pitch_list("b c c f f b f b f b")
t8.reach("BB")
t8.advance(3, "34 1B")

# 2. BOS #18 Shane Victorino (X - X - 2)
t8.new_ab()
t8.pitch_list("b c f")
t8.out("P6")

# 3. BOS #15 Dustin Pedroia (X - X - 2)
t8.new_ab()
t8.pitch_list("1 b b 1")
t8.out("F8")

# 4. BOS #34 David Ortiz (X - X - 2)
t8.new_ab()
t8.pitch_list("c")
t8.hit(1)

# Pitching change (HOU): #35 Josh Fields replaces #53 Wesley Wright
t8.pitching_substitution(35)

# 5. BOS #12 Mike Napoli (2 - X - 34)
t8.new_ab(is_risp=True)
t8.pitch_list("b b s d s t")
t8.out("KT")


# Bot 8th
# Pitching: BOS #32 Craig Breslow
b8 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #36 Junichi Tazawa
b8.pitching_substitution(32)

# 4. HOU #15 Jason Castro (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("L8")

# 5. HOU #23 Chris Carter (X - X - X)
b8.new_ab()
b8.pitch_list("c s b t")
b8.out("KT")

# 6. HOU #29 Brett Wallace (X - X - X)
b8.new_ab()
b8.pitch_list("b b f b b")
b8.reach("BB")
b8.thrown_out(2, "30 CS", 3, 32)

# 7. HOU #30 Matt Dominguez (X - X - 29)
b8.new_ab()
b8.pitch_list("c b")
b8.no_ab("CS")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: HOU #35 Josh Fields
t9 = game.new_inning()

# 6. BOS #5  Jonny Gomes (X - X - X)
t9.new_ab()
t9.pitch_list("c c b t")
t9.out("KT")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t9.new_ab()
t9.pitch_list("c f f s")
t9.out("K")

# 8. BOS #7  Stephen Drew (X - X - X)
t9.new_ab()
t9.pitch_list("b c b c f s")
t9.out("K")

# Winning team: HOU
# WP: HOU #39 Brett Oberholtzer
game.winning_pitcher(39)
# SV: HOU #35 Josh Fields
game.save_pitcher(35)

# Loser team: BOS
# LP: BOS #41 John Lackey
game.losing_pitcher(41, is_away_team=True)

# print(game)
game.generate_scorecard()
