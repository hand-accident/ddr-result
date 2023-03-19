<script>
    let className;
    export { className as class };
</script>

<div class="a {className}">
    <slot />
</div>

<style lang="postcss" module>
    .a {
        @apply relative flex flex-col rounded-box /*card*/
        bg-base-100 snap-start;
    }
    .a:focus {
        @apply outline-none;
    }
</style>
