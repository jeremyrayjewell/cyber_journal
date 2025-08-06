SUMMARY OF 
**LINUX BASICS FOR HACKERS** 
(FIRST EDITION) BY OCCUPYTHEWEB

---

# CHAPTER 4: ADDING AND REMOVING SOFTWARE

---

This chapter introduces us to our *package/software manager* and to *software packages*. Linux dstros use package managers to install software packages. Here my use of Arch causes some deviation from the book, as Arch uses the `pacman` package manager while Kali uses `apt`. Furthermore, Kali's Debian `apt` package manager has newer shorted commands, i.e. `apt` vs `apt-get`. These newer commands date from 2015, yet the book mostly prefers the older ones (probably for broader compatibility). I will try to reflect those updates here, as well as my Arch experience. It is still good to know the book's older syntax.

## Using apt to Handle Software

`apt` (*Advanced Packaging Tool*) is the default package manager in Debian systems like Linux. Its primary command as idnetified in the book is `apt-get`, although since 2015 `apt`has also worked.

### Searching for a Package

Your package manager uses *repositories* to fetch package metadata and software archives, enabling it to automatically install, update, and resolve dependencies for all your software. Repositories are servers holding the software available for your specific Linux distro. We can use the package manager's search tool to confirm that the desired package is available.

- Debian: `apt search <keyword>`

- Arch: `pacman -Ss <keyword>`

Running these commands give us a list of packages whose names or descriptions match our query. Though the book uses the example of searching for `snort`, we could also refine our search criteria to something like `snort intrusion` to get better results.

### Adding Software

To add software from your distro's default repository, use the following commands:

- Debian: `apt install <packagename>`

- Arch: `pacman -S <packagename>`
	
### Removing Software

To remove software from your system, use the following commands:

- Debian: `apt remove <packagename>`

- Arch: `pacman -R <packagename>`

`remove` doesn't remove configuration files, which would allow you to reinstall the same software in the future without losing your previous configurations. If you want to remove those configurations, you can use the `purge` command in Debian or in Arch by adding the `-n`/`--nosave` option to the `pacman -R`/`--remove` command:

- Debian: `apt purge <packagename>`

- Arch: `pacman -Rn <packagename>`

While Debian's `purge` option removes configurations, it doesn't remove dependencies. To remove automatically installed dependencies which are no longer required by any manually installed package after said package has been removed with `remove` or `purge`, we can run `autoremove`. Its Arch `pacman` counterpart is `-s`/`--recursive`

- Arch: `pacman -Rns <packagename>` [also cleans up dependencies]

- Debian: `apt autoremove <packagename>`

Beyond what is said in the book, it is worth noting that `autoremove` with no packagename argument will remove all automatically installed packages that no manually installed package currently needs. Such a universal clean-up command also exists in Arch.

- Debian: `apt autoremove` [universal]

- Arch: `pacman -Rns $(pacman -Qdtq)` [universal]

### Updating Packages

*Updating* refers to fetching the latest package lists from your configured repositories. It **doesn't install anything**, it just checks what's new.

- Debian: `apt update`

- Arch: `pacman -Sy`

As we have seen before with software removal, Arch's minimal, unified design allows flexible commands with more flexible flags. Just as we can run the `-Rns` options to achieve the same as separate Debian commands `remove`, `purge`, and `autoremove`, we can also update and upgrade with just `Syu` in Arch.

### Upgrading Packages

Upgrading actually installs the newer versions of installed packages. To remain current, updating is needed first.

- Debian: `apt upgrade`

- Arch: `pacman -Syu` [updates & upgrades]

## Adding Repositories to Your sources.list File

Not all software you may want will be available in the default repositories. Your system's repositories are stored in a specific file, which can be edited in a text editor like `leafpad` to add or remove repositories.

- Debian: `leafpad /etc/apt/sources.list`

- Arch: `leafpad /etc/pacman.conf`

The book provides the following Debian repo categories:

- `main` - fully supported open-source

- `universe` - community-maintained

- `multiverse` - restricted-by-law

- `restricted` - proprietary drivers

- `backports` - newer releases back-ported

<pre markdown>
Tip: Don't enable `testing`, `unstable` or `experimental` repos unless you're prepared to deal with breakages.
</pre>

**Arch's** repositories work on a much simpler model: a small set of curated repos (`core`/`extra`/`community`) and the vast AUR (Arch User Repository) community archive.

## Using a GUI-based Installer

GUI installers aren’t included by default on recent Kali releases, but you can add one via APT.

Install Synaptic (or GDebi) with:
<pre markdown>
sudo apt-get update
sudo apt-get install synaptic
</pre>

Launch it from the Settings menu (“Synaptic Package Manager”).

Search for your package (e.g. “snort”), tick its checkbox, then click Apply. Synaptic will pull in the package plus any missing dependencies and install them via the GUI.

## Installing Software with git

If a tool isn’t in any APT (or Pacman) repo—often because it’s brand-new or niche—you can fetch it directly from its GitHub repository. Go to https://github.com and search for the project name (e.g. “bluediving”). Clone the repo in your terminal by running:

`git clone https://github.com/balle/bluediving.git`

This copies all files into a new `bluediving/` folder. Verify the download with `ls -l`. You should see a directory named bluediving alongside your other folders. Once cloned, you can enter the new directory and follow its README to build or install the software.

## Summary

This chapter covered the three essential ways to get new tools on your Linux box: using the distro's package manager, a GUI, and cloning directly from GitHub.

## Exercises

Package manager practice: install a new package from the default repo and remove it, update your repository and upgrade your software packages.

Git practice: find and clone a tool on GitHub and verify its presence. 

---

## Summary author: **Jeremy Ray Jewell**
[GitHub](https://github.com/jeremyrayjewell)
[LinkedIn](https://www.linkedin.com/in/jeremyrayjewell)
