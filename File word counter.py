def count_file_stats(filename):
    with open(filename,'r',encoding = 'utf-8') as file:
        content = file.read();
    words = content.split();
    num_words = len(words);
    num_chars = len(content);
    num_lines = len(content.splitlines());
    return num_words , num_chars , num_lines;
filename = input("enter file name:");
w , c , l = count_file_stats(filename);
print("\n--- file statistics for '{filename}' ---");
print(f"woords: {w} | characters: {c} | lines: {l}");
