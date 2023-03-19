<script>
    import Link from "$c/Link.svelte";
    export let href;
</script>

<Link {href} class=""><slot /></Link>
