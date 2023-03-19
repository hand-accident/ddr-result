<script>
    import Bio from "../layout/Bio.svelte";
    import Footer from "../layout/Footer.svelte";
    import Link from "../layout/Link.svelte";
    import iconImage from "./icon.webp";
    const links = {
        twitter: "https://twitter.com/hand_accident",
        github: "https://github.com/hand-accident",
        "3icecream": "https://3icecream.com/profile/haxident",
        skillattack:
            "http://skillattack.com/sa4/dancer_profile.php?ddrcode=51449631",
    };
</script>

<Footer>
    <svelte:fragment slot="bio">
        <Bio src={iconImage}>hand_accident | JQOH | r1amu</Bio>
    </svelte:fragment>
    <svelte:fragment slot="links">
        {#each Object.entries(links) as [disp, href]}
            <Link {href}>{disp}</Link>
        {/each}
    </svelte:fragment>
</Footer>
